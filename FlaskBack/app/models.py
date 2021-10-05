from sqlalchemy import PrimaryKeyConstraint
from app import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    is_admin = db.Column(db.Integer)
    username = db.Column(db.String(64))
    balance = db.Column(db.Float)
    army_id = db.Column(db.Integer, db.ForeignKey("army.id"))


class AchievementManager(db.Model):
    __tablename__ = 'achievement_manager'
    __table_args__ = (PrimaryKeyConstraint('medal_id', 'user_id'),)
    medal_id = db.Column(db.Integer, db.ForeignKey('medals.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)


class Medals(db.Model):
    __tablename__ = 'medals'
    id = db.Column(db.Integer, primary_key=True, index=True)
    medal_type = db.Column(db.String(32))


class Army(db.Model):
    __tablename__ = 'army'
    id = db.Column(db.Integer, primary_key=True, index=True)
    infantry_id = db.Column(db.Integer, db.ForeignKey("infantry.id"))
    tanks_id = db.Column(db.Integer, db.ForeignKey("tanks.id"))
    airplanes_id = db.Column(db.Integer, db.ForeignKey("airplanes.id"))
    fleet_id = db.Column(db.Integer, db.ForeignKey("fleet.id"))
    info = db.relationship("ArmyInfo", backref="army", lazy=True)


class ArmyInfo(db.Model):
   __tablename__ = 'army_info'
   id = db.Column(db.Integer, primary_key=True, index=True)
   army_id = db.Column(db.Integer, db.ForeignKey("army.id"))
   info = db.Column(db.String(64))


class Infantry(db.Model):
    __tablename__ = 'infantry'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)


class Tanks(db.Model):
    __tablename__ = 'tanks'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)


class Airplanes(db.Model):
    __tablename__ = 'airplanes'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)


class Fleet(db.Model):
    __tablename__ = 'fleet'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)
