from app import db

class ItemsModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, supplier, name, quantity, price):
        self.supplier = supplier
        self.name = name
        self.quantity = quantity
        self.price = price
