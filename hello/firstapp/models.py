from django.db import models
# from django.db.models import F


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


"""query()"""
# people = Person.objects.filter(name="Bob").exclude(age=34)
# print(people.query)

"""delete()"""
# Person.objects.filter(id=4).delete()

# person = Person.objects.get(id=2)
# person.delete()

"""update_or_create()"""
# values_for_update = {"name": "Bob", "age": 31}
# bob, created = Person.objects.update_or_create(id=2, defaults=values_for_update)

"""update()"""
# Person.objects.all().update(name="Mike")
# Person.objects.all().update(age=F("age") + 1)

# Person.objects.filter(id=1).update(name="Mike")

"""save()"""
# bob = Person.objects.get(id=2)
# bob.name = "Bobic"
# bob.save(update_fields=["name"])

# bob = Person.objects.get(id=2)
# bob.name = "Bob"
# bob.save()

"""in_bulk()"""
# people2 = Person.objects.in_bulk([1, 5])
# for id in people2:
#     print(people2[id].name)
#     print(people2[id].age)

# for id in people:
#     print(people[id].name)
#     print(people[id].age)

"""exclude()"""
# people = Person.objects.exclude(age=27)
# print(people)

"""filter()"""
# people = Person.objects.filter(age=23)
# print(people)
#
# people2 = Person.objects.filter(name="Bob", age=24)
# print(people2)

"""all()"""
# people = Person.objects.all()
# print(people)

"""create()"""
# tom = Person.objects.create(name="Tom", age=23)

"""save()"""
# bart = Person(name="Bart", age=27)
# # bart.save()

"""get()"""
# tom = Person.objects.get(name="Tom")
# bob = Person.objects.get(age=23)
# tim = Person.objects.get(name="Tim", age=23)
# bart = Person.objects.get(name="Bart")

"""get_or_create()"""
# bob, created = Person.objects.get_or_create(name="Bob", age=24)
# print(bob.name)
# print(bob.age)
