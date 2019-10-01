from application import db
from application.models import Base
from sqlalchemy.sql import text

sports = db.Table('sports',
    db.Column('sport_id', db.Integer, db.ForeignKey('sport.id'), primary_key=True),
    db.Column('club_id', db.Integer, db.ForeignKey('club.id'), primary_key=True)
)

class Club(Base):
    
    name = db.Column(db.String(40), unique=True, nullable=False)
    city = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(40))
    email = db.Column(db.String(40))
    tel = db.Column(db.String(40))
    price = db.Column(db.Integer, nullable=False)

    sports = db.relationship('Sport', secondary=sports, lazy='subquery',
        backref=db.backref('clubs', lazy=True))

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
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) as reviews, ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "GROUP BY club.id "
                    "ORDER BY (CASE WHEN ROUND(AVG(review.grade), 2) is NULL THEN 1 ELSE 0 END), average DESC;")
        result = db.engine.execute(stmt)
        
        return result

    @staticmethod
    def my_clubs_by_avg_grade(account_id):
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, review.id AS review_id, review.account_id AS user_id, COUNT(review.grade) as reviews, ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "WHERE club.account_id = :id "
                    "GROUP BY club.id, review.id "
                    "ORDER BY (CASE WHEN ROUND(AVG(review.grade), 2) is NULL THEN 1 ELSE 0 END), average DESC").params(id=account_id)
        result = db.engine.execute(stmt)

        return result





    