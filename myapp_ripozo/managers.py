import re

from ripozo.resources.fields.common import StringField, IntegerField
from ripozo_sqlalchemy import AlchemyManager, ScopedSessionHandler

from myapp.models import DB, User, UserGroup, Group


class FlaskSqlalchemySessionHandler(object):
    """
    This it just a mechanism for getting the session handler.  It
    will at some point be integrated into ripozo-sqlalchemy
    """

    def get_session(self):
        return DB.session

    @staticmethod
    def handle_session(session, exc=None):
        pass  # Not necessary with flask sqlalchemy handler


SESSION_HANDLER = FlaskSqlalchemySessionHandler()


class UserManager(AlchemyManager):
    model = User
    fields = ('id', 'username', 'first_name')
    create_fields = ('username', 'first_name')
    update_fields = ('first_name',)
    _field_validators = {
        # username must be between 3 and 20 alphanumeric characters
        'username': StringField('username', minimum=3, regex=re.compile(r'^[a-zA-Z0-9]{3,20}'), required=True),
        'first_name': StringField('first_name', required=True)
    }


class GroupManager(AlchemyManager):
    model = Group
    fields = ('id', 'name', 'users.id', 'users.username', 'users.first_name')
    create_fields = ('name',)
    update_fields = tuple()
    list_fields = ('id', 'name',)
    _field_validators = {
        'name': StringField('name', minimum=3, maximum=20),
        'id': IntegerField('id')
    }


class UserGroupManager(AlchemyManager):
    model = UserGroup
    fields = ('user_id', 'group_id')
    create_fields = ('user_id', 'group_id',)
    update_fields = tuple()
    list_fields = ('user_id', 'group_id')
    _field_validators = {
        'user_id': StringField('user_id', required=True),
        'group_id': StringField('group_id', required=True)
    }
