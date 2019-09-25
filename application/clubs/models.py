from application import db
from application.models import Base
from sqlalchemy.sql import text

class Club(Base):
    
    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80))
    email = db.Column(db.String(100))
    tel = db.Column(db.String(20))
    price = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    reviews = db.relationship("Review", backref='club', lazy=True)

    def __init__(self, name, city, address, email, tel, price):
        self.name = name
        self.city = city
        self.address = address
        self.email = email
        self.tel = tel
        self.price = price

    @staticmethod
    def clubs_by_avg_grade():
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, AVG(review.grade) AS average FROM club LEFT JOIN review ON review.club_id = club.id GROUP BY club.id ORDER BY average DESC;")
        result = db.engine.execute(stmt)
        print(type(result))

        return result




    