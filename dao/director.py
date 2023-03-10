from dz_18.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session
        self.model = Director

    def get_by_id(self, did):
        return self.session.query(self.model).get(did)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, data):
        director = self.model(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_by_id(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, data):
        director = self.get_by_id(data['id'])
        director.name = data['name']
        self.session.add(director)
        self.session.commit()
