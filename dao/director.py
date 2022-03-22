from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).filter(Director.id == did).one()

    def get_all(self):
        return self.session.query(Director).all()

    def create(self,data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def update(self, data):
        did = data.get("id")
        director = self.session.query(Director).filter(Director.id == did).update(data)
        self.session.commit()

        return director

    def update_partial(self, data):
        pass


    def delete(self,did):
        self.session.query(Director).filter(Director.id == did).delete()
        self.session.commit()