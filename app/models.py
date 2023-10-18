from app import db

class CategoriesModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'

class ItemsModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('CategoriesModel', backref='items')

    def __repr__(self):
        return f'<Item {self.name}>'
