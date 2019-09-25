from application import db
from application.models import Base
from sqlalchemy.sql import text

class Review(Base):

    grade = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    
    def __init__(self, grade, review):
        self.grade = grade
        self.review = review

    @staticmethod
    def get_users_reviews(user_id):
        stmt = text("SELECT * FROM review LEFT JOIN club ON review.club_id = club.id WHERE review.account_id = :id").params(id=user_id)
        result = db.engine.execute(stmt)

        return result

        