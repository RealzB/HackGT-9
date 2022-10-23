from mongoengine import Document, StringField, IntField, ListField

class Sounds(Document):
    name = StringField


class Spaces(Document):
    name = StringField

class test(Document):
    audio = StringField