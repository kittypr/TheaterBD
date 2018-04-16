from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    birth = db.Column(db.DateTime)
    hire_date = db.Column(db.DateTime)
    sex = db.Column(db.String(1))
    payment = db.Column(db.Integer)
    children = db.Column(db.Integer)

    def __repr__(self):
        return '<Employee: {} - {}>'.format(self.id, self.name)


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return self.name


class Voice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return self.name


class Actor(db.Model):
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    voice_range = db.Column(db.Integer, db.ForeignKey('voice.id'))
    best_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))

    def __repr__(self):
        return '<Actor: {} - {}>'.format(self.employee_id, self.voice_range, self.best_genre)
