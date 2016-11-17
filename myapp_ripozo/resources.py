from ripozo import restmixins, ListRelationship, Relationship

from myapp_ripozo.managers import SESSION_HANDLER, UserManager, UserGroupManager, GroupManager


class UserResource(restmixins.CRUDL):
    """
    CRUDL= Create, Retrieve, Update, Delete, and List
    It handles it based on the route + method
    """
    append_slash = True
    pks = ('id',)
    resource_name = 'user'
    manager = UserManager(SESSION_HANDLER)
    _relationships = (
        ListRelationship('groups', relation='GroupResource', embedded=True),
    )


class GroupResource(restmixins.CRUDL):
    append_slash = True
    pks = ('id',)
    resource_name = 'group'
    manager = GroupManager(SESSION_HANDLER)
    _relationships = (
        ListRelationship('users', relation='UserResource', embedded=True),
    )


class UserGroupResource(restmixins.Create):
    append_slash = True
    pks = ('user_id', 'group_id',)
    resource_name = 'user_group'
    manager = UserGroupManager(SESSION_HANDLER)
    _relationships = (
        Relationship('user', property_map=dict(user_id='id'), relation='UserResource'),
        Relationship('group', property_map=dict(group_id='id'), relation='GroupResource'),
    )
