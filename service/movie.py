from app.dao.movie import  MovieDAO


class  MovieService:
    def __init__(self, dao:  MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_movies_by_director(self, data):
        return self.dao.get_movies_by_director(data)

    def get_movies_by_year(self, data):
        return self.dao.get_movies_by_year(data)

    def get_movies_by_genre_id(self, data):
        return self.dao.get_movies_by_genre(data)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def update_partial(self, data):
        pass

    def delete(self, mid):
        return self.dao.delete(mid)
