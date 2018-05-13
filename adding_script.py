from app import db
from models import Genre, Voice, Employee, Actor, Award
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
a = Actor(employee_id=e.id, height=186, weight=84, voice_range=7, best_genre=1, about='I started my career at 16 in '
                                                                                      'Maine. Now I can say proudly '
                                                                                      'I have found my place - the '
                                                                                      'wonderful Red Theatre. Welcome!')
db.session.add(a)


# second empl - act
e = Employee(name="Anna Sui", birth=datetime(1972, 4, 27),
             hire_date=datetime(2005, 2, 4), sex='f', payment=1300, children=0)
db.session.add(e)
db.session.commit()
a = Actor(employee_id=e.id, height=173, weight=58, voice_range=1, best_genre=2, about='My job is my passion, you '
                                                                                      'can see it on stage. Hope '
                                                                                      'you enjoy my characters as much '
                                                                                      'as I do.')
db.session.add(a)


# third empl - act
e = Employee(name="Victoria Langley", birth=datetime(1985, 8, 12),
             hire_date=datetime(2010, 2, 4), sex='f', payment=1000, children=0)
db.session.add(e)
db.session.commit()
a = Actor(employee_id=e.id, height=165, weight=45, voice_range=3, best_genre=3, about='Every comedy has a little traged'
                                                                                      'y, so we respect comedy actors '
                                                                                      'a bit more, ha-ha! Come and '
                                                                                      'watch I and other awesome '
                                                                                      'actors play comedies for you!')
db.session.add(a)


awrd = Award(actor_id=1, award="Best male actor of Texas 2012", date=datetime(2012, 12, 12))
db.session.add(awrd)
awrd = Award(actor_id=1, award="Best male actor of Texas 2008", date=datetime(2008, 12, 12))
db.session.add(awrd)
awrd = Award(actor_id=1, award="Best male actor of Texas 1999", date=datetime(1999, 12, 15))
db.session.add(awrd)
awrd = Award(actor_id=1, award="Best male actor of Texas 2000", date=datetime(2000, 12, 12))
db.session.add(awrd)
awrd = Award(actor_id=1, award="Majestic Theatre: contribution to Art", date=datetime(2000, 6, 21))
db.session.add(awrd)
awrd = Award(actor_id=2, award="Majestic Theatre: contribution to Art", date=datetime(2015, 9, 12))
db.session.add(awrd)
awrd = Award(actor_id=3, award="Majestic Theatre: young talent", date=datetime(2004, 9, 3))
db.session.add(awrd)


db.session.commit()


actors = Actor.query.all()

for actor in actors:
    print(actor.employee_id,
          Genre.query.get(actor.best_genre), Voice.query.get(actor.voice_range), actor.height, actor.weight)
