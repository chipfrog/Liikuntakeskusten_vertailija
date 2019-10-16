from application import db
from sqlalchemy import text

class Base (db.Model):

    __abstract__= True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


    @staticmethod
    def general_info():
        stmt = text("SELECT COUNT(DISTINCT account.id) AS users, COUNT(DISTINCT club.id) AS clubs, "
                "COUNT(DISTINCT club.city) AS cities "
                "FROM account, club;")
    
        res = db.engine.execute(stmt)
        result = []
        
        for row in res:
            result.append(row)

        return result    
