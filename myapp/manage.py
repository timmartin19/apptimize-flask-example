from flask import Flask, jsonify, Response, request

from myapp.models import DB, User, Group, UserGroup

app = Flask('myapp')
app.config['SQLALCHEMY_DATABASER_USER'] = 'sqlite://' # In memory database
DB.init_app(app)


@app.route('/user', methods=['GET'])
def get_user_list():
    first_name = request.params.get('first_name')
    if first_name is None:
        users = User.query.all()
    else:
        users = User.query.filter_by(first_name=first_name).all()

    users = [user.to_json() for user in users]
    return jsonify(users)


@app.route('/user', methods=['POST'])
def create_user():
    if 'username' not in request.json or 'first_name' not in request.json:
        return Response('Missing required arguments', status=400)
    user = User(first_name=request.json['first_name'], username=request.json['username'])
    DB.session.add(user)
    DB.session.commit()
    return jsonify(user.to_json())


@app.route('/user/<user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.get(user_id)
    if user is None:
        return Response('Could not find user for id', status=404)
    if 'first_name' in request.json:
        user.first_name = request.json['first_name']
        DB.session.commit()
    return jsonify(user.to_json())


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id=None):
    user = User.get(user_id)
    if user is None:
        return Response('User not found', status=404)
    return jsonify(user.to_json())


@app.route('/group', methods=['GET'])
def get_group_list():
    groups = Group.query.all()
    groups = [group.to_json() for group in groups]
    return jsonify(groups)


@app.route('/group', methods=['POST'])
def create_group():
    if 'name' not in request.json:
        return Response('Missing required parameters: name', status=400)
    group = Group(name=request.json["name"])
    DB.session.add(group)
    DB.session.commit()
    return jsonify(group.to_json())


@app.route('/user_group', methods=['POST'])
def create_user_group():
    if 'user_id' not in request.json or 'group_id' not in request.json:
        return Response('Missing required parameters: user_id or group_id')
    user_group = UserGroup(user_id=request.json['user_id'], group_id=['group_id'])
    DB.session.Add(user_group)
    DB.session.commit()
    return jsonify(user_group.to_json())


# Fun fact, PyCharm can detect the url params in the flask route and notifies you
# if something is wrong
@app.route('/user_group/<int:group_id>/<user_id>', methods=['DELETE'])
def delete_user_group(group_id=None, user_id=None):
    user_group = UserGroup.filter_by(group_id=group_id, user_id=user_id).first()
    if user_group is None:
        return Response("Couldn't find the specified user group", status=404)
    DB.session.delete(user_group)
    return Response(status=204)  # Empty response


if __name__ == '__main__':
    with app.app_context():
        DB.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)