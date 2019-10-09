from application import db
from application.models import Base

class User(Base):

    __tablename__= "account"

    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    
    clubs = db.relationship("Club", backref='account', lazy=True)
    reviews = db.relationship("Review", backref='account', lazy=True)

    def __init__(self, name, email, username, password, role):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.role = role
        
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_role(self):
        return self.role    

                          