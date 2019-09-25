from application import db
from application.models import Base

class User(Base):

    __tablename__= "account"

    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(144), nullable=False)
    
    clubs = db.relationship("Club", backref='account', lazy=True)
    reviews = db.relationship("Review", backref='account', lazy=True)

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

                          