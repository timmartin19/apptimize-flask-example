from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class UserGroup(DB.Model):
    __tablename__ = 'user_group_m2m'
    user_id = DB.Column(DB.String, DB.ForeignKey('user.id'), primary_key=True)
    group_id = DB.Column(DB.Integer, DB.ForeignKey('group.id'), primary_key=True)

    def to_json(self):
        return dict(user_id=self.user_id, group_id=self.group_id)


class Group(DB.Model):
    # These are columns
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String, unique=True)

    # This is an accessor that uses the M2M table
    users = DB.relationship("User", secondary=UserGroup.__table__, backref="groups")

    def to_json(self):
        return dict(id=self.id, name=self.name)


class User(DB.Model):
    id = DB.Column(DB.String, default=lambda: str(uuid4()), primary_key=True)
    username = DB.Column(DB.String, unique=True)
    first_name = DB.Column(DB.String, nullable=False)

    def to_json(self):
        return dict(id=self.id, username=self.username, first_name=self.first_name)
