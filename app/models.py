from app import db, login_manager
from flask_login import UserMixin



#Oauth decorators for social media login
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)  

    bodyweight = db.relationship('Bodyweight', backref='author', lazy='dynamic')

    hangboardwerk = db.relationship('HangboardWerk', backref='author', lazy='dynamic')
    kampuswerkouts = db.relationship('KampusWerkout', backref='author', lazy='dynamic')
    circuitmoves = db.relationship('CircuitMoves', backref='author', lazy='dynamic')
    blocs = db.relationship('Blocs', backref='author', lazy='dynamic')
    routes = db.relationship('Routes', backref='author', lazy='dynamic')




class HangboardWerk(db.Model):

    __tablename__ = "hangboardwerk"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    board = db.Column(db.String(96))
    holds_used = db.Column(db.Integer)
    arm_used = db.Column(db.String(96))
    hangtime = db.Column(db.Integer)
    resttime = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    setrest = db.Column(db.Integer)
    weight_kg = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, board, holds_used, reps, sets, setrest, arm_used, hangtime, resttime, weight_kg, timestamp, user_id):
        self.name = name
        self.board = board
        self.holds_used = holds_used
        self.arm_used = arm_used
        self.hangtime = hangtime
        self.resttime = resttime
        self.reps = reps
        self.sets = sets
        self.setrest = setrest
        self.weight_kg = weight_kg
        self.timestamp = timestamp
        self.user_id = user_id

    def as_dict (self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class KampusWerkout(db.Model):
    __tablename__ = "kampuswerkout"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    kampuslog = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __init__(self, name, kampuslog, timestamp, user_id):
        self.name = name
        self.kampuslog = kampuslog
        self.timestamp = timestamp
        self.user_id = user_id

    def as_dict (self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CircuitMoves(db.Model):

    __tablename__ = "circuitmoves"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    numberofmoves = db.Column(db.Integer)
    intensity = db.Column(db.Integer)
    werktime = db.Column(db.Integer)
    grade = db.Column(db.String(4096))
    comments = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, numberofmoves, intensity, werktime, grade, comments, timestamp, user_id):
        self.name = name
        self.numberofmoves = numberofmoves
        self.intensity = intensity
        self.werktime = werktime
        self.grade = grade
        self.comments = comments
        self.timestamp = timestamp
        self.user_id = user_id
    def as_dict (self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}        

class Routes(db.Model):

    __tablename__ = "routes"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    height = db.Column(db.Integer)
    intensity = db.Column(db.Integer)
    werktime = db.Column(db.Integer)
    grade = db.Column(db.String(96))
    venue = db.Column(db.String(96))
    angle = db.Column(db.String(96))
    style = db.Column(db.String(96))
    comments = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, height, intensity, werktime, grade, venue, angle, style, comments, timestamp, user_id):
        self.name = name
        self.height = height
        self.intensity = intensity
        self.werktime = werktime
        self.grade = grade
        self.venue = venue
        self.angle = angle
        self.style = style
        self.comments = comments
        self.timestamp = timestamp
        self.user_id = user_id
    def as_dict (self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Blocs(db.Model):

    __tablename__ = "blocs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(4096))
    intensity = db.Column(db.Integer)
    werktime = db.Column(db.Integer)
    grade = db.Column(db.String(96))
    venue = db.Column(db.String(96))
    angle = db.Column(db.String(96))
    style = db.Column(db.String(96))
    comments = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, intensity, werktime, grade, venue, angle, style, comments, timestamp, user_id):
        self.name = name
        self.intensity = intensity
        self.werktime = werktime
        self.grade = grade
        self.venue = venue
        self.angle = angle
        self.style = style
        self.comments = comments
        self.timestamp = timestamp
        self.user_id = user_id
    def as_dict (self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Bodyweight(db.Model):

    __tablename__ = "bodyweight"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    bodyweight_kg = db.Column(db.Float)
    notes = db.Column(db.String(4096))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, bodyweight_kg, notes, timestamp, user_id):
        self.name = name
        self.bodyweight_kg = bodyweight_kg
        self.notes = notes
        self.timestamp = timestamp
        self.user_id = user_id