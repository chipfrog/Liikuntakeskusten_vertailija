from application import db
from application.models import Base
from sqlalchemy import text

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

    @staticmethod
    def clubs_reviewed(account_id):
        stmt = text("SELECT review.club_id, review.id AS review_id FROM review "
                    "WHERE review.account_id = :account_id").params(account_id=account_id)
        res = db.engine.execute(stmt)
        dictionary = {}
        for row in res:
            dictionary[row[0]] = row[1]

        return dictionary

    @staticmethod
    def user_info(account_id):
        stmt = text("SELECT *, COUNT(review.id) AS reviews FROM account"
                    "LEFT JOIN review ON review.account_id = account.id "
                    "WHERE review.account_id = :id").params(id=account_id)
        res = db.engine.execute(stmt)

        return res                    

                          

                          