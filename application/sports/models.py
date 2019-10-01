from application import db
from application.models import Base

class Sport(Base):
    name = db.Column(db.String(30), nullable=False)
    
    def __init__(self, name):
        self.name = name
