import datetime
import os

from peewee import MySQLDatabase, Model, CharField, TextField, DateTimeField

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"), host=os.getenv("MYSQL_HOST"), port=3306)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])
