from mongoengine import *


class Venue(EmbeddedDocument):
    name = StringField(required=True)
    city = StringField()
    country = StringField()
    dive_rating = IntField(min=1, max=5)
