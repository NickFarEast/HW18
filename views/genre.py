from flask_restx import Resource, Namespace

from app.dao.model.genre import GenresSchema
from app.implemented import genre_service


from flask import request

genres_ns = Namespace('genres')

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Функция для отображения всех жанров в базе"""
        all_genres = genre_service.get_all()

        return genres_schema.dumps(all_genres), 200

    def post(self):
        """Функция для записи нового жанра в базу"""
        req_jason = genre_schema.load(request.json)
        genre_service.create(req_jason)
        return "", 201


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """Функция для получения жанра из базы по ID"""
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    def put(self, gid):
        """Функция для внесения изменения в базу по ID"""
        req_jason = genre_schema.load(request.json)
        req_jason["id"] = gid

        genre_service.update(req_jason)

        return "", 204

    def delete(self, gid):
        """Функция для удаления из базы по ID"""
        genre_service.delete(gid)
        return "", 204