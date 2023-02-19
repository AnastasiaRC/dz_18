from flask_restx import Resource, Namespace
from dz_18.dao.model.genre import GenreSchema
from dz_18.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        genre_data = GenreSchema().dump(genre)
        return genre_data, 200
