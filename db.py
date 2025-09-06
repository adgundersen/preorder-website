from peewee import *

db = SqliteDatabase('people.db')

class User(Model):
    email = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.