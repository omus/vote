from vote import app, db


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    votes = db.relationship('Vote', backref='user', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.id in app.config["ADMIN_USERS"]

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Option(db.Model):
    name = db.Column(db.String(128), primary_key=True)
    premium = db.Column(db.Boolean, default=False)
    votes = db.relationship('Vote', backref='option', lazy='dynamic')

    def __repr__(self):
        return '<Option {}>'.format(self.name)


class Vote(db.Model):
    option = db.Column(db.String(128), primary_key=True)
    rank = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey('option.name'),
                          primary_key=True)

    def __repr__(self):
        return '<Vote {}: {}>'.format(self.option, self.score)

