from flask import Flask, request
from flask_restful import Resource, Api
import settings
import mongoengine as mongo

from resources.gig import Gigs


app = Flask(__name__)
api = Api(app)

mongo.connect(
    settings.MONGO['DATABASE'],
    host=settings.MONGO['HOST'],
    port=settings.MONGO['PORT'],
    username=settings.MONGO['USERNAME'],
    password=settings.MONGO['PASSWORD']
)

api.add_resource(Gigs, '/gigs', endpoint='All gigs')


if __name__ == "__main__":
    app.run(debug=settings.DEBUG)