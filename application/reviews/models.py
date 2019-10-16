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
    def get_users_reviews(user_id, limit, offset):
        stmt = text("SELECT review.id AS review_id, review.grade, review.review, review.club_id, club.name, club.city "
                    "FROM review LEFT JOIN club ON review.club_id = club.id "
                    "WHERE review.account_id = :id "
                    "ORDER BY review.date_modified DESC "
                    "LIMIT :limit OFFSET :offset").params(id=user_id, limit=limit, offset=offset)
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def get_users_review_ids(user_id):
        stmt = text("SELECT club.id FROM review "
                    "LEFT JOIN club ON review.club_id = club.id "
                    "WHERE review.account_id = :id").params(id = user_id)    
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)
        
        return result

    @staticmethod
    def get_clubs_reviews(club_id):
        stmt = text("SELECT review.grade, review.review, review.date_modified AS review_modified, account.username FROM review "
                    "INNER JOIN club ON review.club_id = club.id "
                    "INNER JOIN account ON account.id = review.account_id "
                    "WHERE club.id = :id "
                    "ORDER BY review.date_modified DESC").params(id=club_id)
        result = db.engine.execute(stmt)
        
        return result    

    


        