from application import db

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80))
    email = db.Column(db.String(100))
    tel = db.Column(db.String(20))
    price = db.Column(db.Integer, nullable=False)

    reviews = db.relationship("Review", backref='club', lazy=True)

    def __init__(self, name, city, address, email, tel, price):
        self.name = name
        self.city = city
        self.address = address
        self.email = email
        self.tel = tel
        self.price = price


    