from flask_restx import Resource, Namespace

from app.dao.model.movie import MoviesSchema

from app.implemented import movie_service

from flask import request

movies_ns = Namespace('movies')

movie_schema = MoviesSchema()
movies_schema = MoviesSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Функция для отображения всех фильмов в базе или с отображением по запросу режиссера, жанра или года выпуска """
        args = request.args

        if 'director_id' in args:
            return movies_schema.dump(movie_service.get_movies_by_director(args['director_id'])), 200
        elif 'year' in args:
            return movies_schema.dump(movie_service.get_movies_by_year(args['year'])), 200
        elif 'genre_id' in args:
            return movies_schema.dump(movie_service.get_movies_by_genre_id(args['genre_id'])), 200
        else:
            return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        """Функция для записи нового фильма в базу"""
        req_jason = movie_schema.load(request.json)
        movie_service.create(req_jason)
        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """Функция для получения фильма из базы по ID"""
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        """Функция для внесения изменения в базу по ID"""
        req_jason = movie_schema.load(request.json)
        req_jason["id"] = mid

        movie_service.update(req_jason)

        return "", 204

    def delete(self, mid):
        """Функция для удаления из базы по ID"""
        movie_service.delete(mid)
        return "", 204
