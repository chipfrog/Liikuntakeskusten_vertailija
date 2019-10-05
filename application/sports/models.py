from application import db
from application.models import Base
from sqlalchemy.sql import text

class Sport(Base):
    name = db.Column(db.String(30), nullable=False)
    
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_sports(club_id):
        stmt = text("SELECT name FROM sports "
                    "LEFT JOIN sport ON sport.id = sports.sport_id "
                    "WHERE sports.club_id = :id").params(id=club_id)

        result = db.engine.execute(stmt)
        return result            

