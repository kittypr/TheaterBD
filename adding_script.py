from app import db
from models import Genre, Voice, Employee, Actor
from datetime import datetime

# clean all
meta = db.metadata
for table in reversed(meta.sorted_tables):
    print('Clear table %s' % table)
    db.session.execute(table.delete())
    db.session.commit()

v = Voice(name="Soprano")
db.session.add(v)
v = Voice(name="Mezzo-soprano")
db.session.add(v)
v = Voice(name="Contralto")
db.session.add(v)
v = Voice(name="Countertenor")
db.session.add(v)
v = Voice(name="Tenor")
db.session.add(v)
v = Voice(name="Baritone")
db.session.add(v)
v = Voice(name="Bass")
db.session.add(v)
print(v.id)
g = Genre(name="Drama")
db.session.add(g)
g = Genre(name="Tragedy")
db.session.add(g)
g = Genre(name="Comedy")
db.session.add(g)


# first empl - act
e = Employee(name="Edward Smith", birth=datetime(1950, 1, 12),
             hire_date=datetime(2000, 4, 17), sex='m', payment=2800, children=0)
db.session.add(e)
db.session.commit()
a = Actor(employee_id=e.id, height=186, weight=84, voice_range=7, best_genre=1)
db.session.add(a)


# second empl - act
e = Employee(name="Anna Sui", birth=datetime(1972, 4, 27),
             hire_date=datetime(2005, 2, 4), sex='f', payment=1300, children=0)
db.session.add(e)
db.session.commit()
a = Actor(employee_id=e.id, height=173, weight=58, voice_range=1, best_genre=2)
db.session.add(a)


db.session.commit()


actors = Actor.query.all()

for actor in actors:
    print(actor.employee_id,
          Genre.query.get(actor.best_genre), Voice.query.get(actor.voice_range), actor.height, actor.weight)
