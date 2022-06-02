from app.db import db, BaseModelMixin

class Crew(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primery_key=True)
    name = db.Column(db.String)
    ship = db.relationship('Ship', backref='Crew', lazy=False, cascade='all,delete-orphan')
    status = db.Column(db.String)
    members = db.relationship('Character',backref='Crew', lazy=False, cascade='all, delete-orphan')

    def __init__(self, name: str, ship: str, status: str, members: list):
        self.name = name
        self.ship = ship
        self.status = status
        self.members = members

    def __repr__(self):
        return f'Crew:({self.name})'
    
    def __str__(self):
        """
        Returns crew's name
        """
        return f'{self.name}'


class Character(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)
    origin = db.Column(db.String)
    crew_id = db.Column(db.Integer, db.ForeignKey('crew.id'), nullable=True)
    devil_fruit_id = db.Column(db.Integer, db.ForeignKey('devilfruit.id'), nullable=True)

    def __init__(self, name, status, origin):
        self.name = name
        self.status = status
        self.origin = origin

    def __repr__(self):
        return f'Character: ({self.name})'
    
    def __str__(self):
        return f'{self.name}'

class DevilFruit(db.Model, BaseModelMixin):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self):
        return f'name: ({self.name})'
    
    def __str__(self):
        return f'{self.name}'