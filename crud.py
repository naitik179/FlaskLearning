from flasksql import dc,Person

##create

myperson=Person('Aish',17)
db.session.add(myperson)
db.session.commit()


##READ

all_persons=Person.query.all()
print(all_persons)

##Select by id
person1=Person.query.get(1)
print(person1.name)


#filter

person_nai=Person.query.filter_by(name='Naitik')
print(person_nai.all())

#Update

firstperson=Person.query.get(1)
firstperson.age=19
db.sesion.add(firstperson)
db.session.commit()


#delete
secondperson=Person.query.get(2)
db.session.delete(secondperson)
db.session.commit()

#print all
all_person123=Person.query.all()
print(all_person123)