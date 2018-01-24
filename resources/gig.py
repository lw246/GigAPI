from flask_restful import Resource
from flask import jsonify, request
import json

from models.gig import Gig


class Gigs(Resource):
    def get(self):
        return json.loads(Gig.objects.all().to_json())

    def post(self):
        data = request.get_json()

        if not data:
            data = {'response': 'ERROR'}
            return jsonify(data)

        gig = Gig(**data)
        gig.save()