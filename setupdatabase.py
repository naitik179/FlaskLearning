from flasksql import db,Person

#creates all the tables model--> DB Tables
db.create_all()


s1=Person('Naitik',20)
s2=Person('RAT',19)

print(s1.id)
print(s2.id)


db.session.add_all([s1,s2])

db.session.commit()

print(s1.id)
print(s2.id)
