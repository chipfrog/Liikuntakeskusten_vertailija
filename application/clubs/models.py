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
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) AS reviews, " 
                    "ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "GROUP BY club.id "
                    "ORDER BY (CASE WHEN ROUND(AVG(review.grade), 2) is NULL THEN 1 ELSE 0 END), average DESC;")
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)
        
        return result

    @staticmethod
    def clubs_by_name():
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) AS reviews, "
                    "ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "GROUP BY club.id "
                    "ORDER BY club.name ASC;")
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def clubs_by_city():
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) AS reviews, "
                    "ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "GROUP BY club.id "
                    "ORDER BY club.city ASC;")
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def clubs_by_price_min():
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) AS reviews, "
                    "ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "GROUP BY club.id "
                    "ORDER BY club.price ASC;")
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def clubs_by_price_max():
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) AS reviews, "
                    "ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "GROUP BY club.id "
                    "ORDER BY club.price DESC;")
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def filter_clubs(city, score, price_min, price_max, sport):
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, "
                    "COUNT(DISTINCT review.grade) as reviews, ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "LEFT JOIN sports ON sports.club_id = club.id "
                    "LEFT JOIN sport ON sport.id = sports.sport_id "
                    "WHERE (:city = '' OR club.city = :city) "
                    "AND (:sport = '' OR sport.name = :sport) "
                    "AND (:price_min IS NULL OR club.price >= :price_min) "
                    "AND (:price_max IS NULL OR club.price <= :price_max) "
                    "GROUP BY club.id "
                    "HAVING :score IS NULL OR ROUND(AVG(review.grade), 2) >= :score "
                    "ORDER BY (CASE WHEN ROUND(AVG(review.grade), 2) is NULL THEN 1 ELSE 0 END), average DESC").params(city=city, score=score, price_min=price_min, price_max=price_max,sport=sport)

        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)
        
        return result       

    @staticmethod
    def my_clubs_by_avg_grade(account_id):
        stmt = text("SELECT club.id AS club_id, club.name, club.city, club.price, COUNT(review.grade) as reviews, ROUND(AVG(review.grade), 2) AS average "
                    "FROM club LEFT JOIN review ON review.club_id = club.id "
                    "WHERE club.account_id = :id "
                    "GROUP BY club.id "
                    "ORDER BY (CASE WHEN ROUND(AVG(review.grade), 2) is NULL THEN 1 ELSE 0 END), average DESC").params(id=account_id)
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def get_club_info(club_id):
        stmt = text("SELECT club.id AS club_id, club.name AS club_name, club.city, club.address, club.email, club.tel, club.price, "
                    "COUNT(DISTINCT review.grade) as reviews, " 
                    "ROUND(AVG(review.grade), 2) AS average, "
                    "COUNT(DISTINCT sports.sport_id) AS sportscount "
                    "FROM club LEFT JOIN review ON review.club_id = club.id LEFT JOIN sports ON sports.club_id = club.id "
                    "WHERE club.id = :id "
                    "GROUP BY club.id").params(id=club_id)
        result = db.engine.execute(stmt)

        return result

    @staticmethod
    def club_has_sport(club_id):
        stmt = text("SELECT sport.name FROM sport "
                    "LEFT JOIN sports ON sports.sport_id = sport.id "
                    "WHERE sports.club_id = :id").params(id = club_id)

        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row.name)

        return result                   

                                 





    