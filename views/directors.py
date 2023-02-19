from flask_restx import Resource, Namespace
from dz_18.dao.model.director import DirectorSchema
from dz_18.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        director_data = DirectorSchema().dump(director)
        return director_data, 200
