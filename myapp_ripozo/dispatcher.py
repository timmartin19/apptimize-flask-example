from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo.adapters import BasicJSONAdapter, HalAdapter

from myapp.models import DB
from myapp_ripozo.resources import UserResource, UserGroupResource, GroupResource

app = Flask('myapp_ripozo')
app.config['SQLALCHEMY_DATABASER_USER'] = 'sqlite://' # In memory database
DB.init_app(app)

dispatcher = FlaskDispatcher(app, url_prefix='/api')
dispatcher.register_adapters(HalAdapter, BasicJSONAdapter)
dispatcher.register_resources(UserResource, UserGroupResource, GroupResource)

if __name__ == '__main__':
    with app.app_context():
        DB.create_all()
    app.run(host='0.0.0.0', debug=True, port=4000)
