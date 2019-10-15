from application import db
from application.models import Base
from sqlalchemy.sql import text

class Sport(Base):
    name = db.Column(db.String(30), nullable=False)
    
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_sports(club_id):
        stmt = text("SELECT name, id FROM sports "
                    "LEFT JOIN sport ON sport.id = sports.sport_id "
                    "WHERE sports.club_id = :id "
                    "ORDER BY name ASC").params(id=club_id)

        result = db.engine.execute(stmt)
        return result

    @staticmethod
    def delete_sport_association(sport_id, club_id):
        stmt = text("DELETE FROM sports "
                    "WHERE sport_id = :sport_id AND club_id = :club_id ").params(sport_id=sport_id, club_id=club_id)

        result = db.engine.execute(stmt)
        return result

                      

