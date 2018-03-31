from mongoengine import *


class Band(EmbeddedDocument):
    name = StringField(required=True)
    songs_played = ListField(StringField())
    rating = IntField(min=0, max=5)
    volume = IntField(min=0, max=11)
    main_act = BooleanField()
    genera = StringField()
