from app import db


class Va(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), index=True, unique=True, nullable=False)
    clients = db.relationship('Client', backref='va', lazy='dynamic')

    def __repr__(self):
        return '<VA: {}>'.format(self.username)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), index=True, nullable=False)
    last_name = db.Column(db.String(25), index=True, nullable=False)
    va_id = db.Column(db.Integer, db.ForeignKey('va.id'))

    def __repr__(self):
        return '<Client: {} {}>'.format(self.first_name, self.last_name)
