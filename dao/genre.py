from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self,data):
        director = Genre(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def update(self, data):
        gid = data.get("id")
        director = self.session.query(Genre).filter(Genre.id == gid).update(data)
        self.session.commit()

        return director

    def update_partial(self, data):
        pass


    def delete(self,gid):
        self.session.query(Genre).filter(Genre.id == gid).delete()
        self.session.commit()