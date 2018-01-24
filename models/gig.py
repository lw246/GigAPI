from mongoengine import *

from models.band import Band
from models.venue import Venue


class Gig(Document):
    venue = EmbeddedDocumentField(Venue)
    bands = EmbeddedDocumentListField(Band)
    date = DateTimeField()
    flavour = StringField()
    rating = IntField(min=1, max=5)
    volume = IntField(min=0, max=11)
