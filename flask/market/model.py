class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    price=db.Column(db.Integer,nullable=False)
    name=db.Column(db.String(length=30),nullable=False,unique=True)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(length=1000),nullable=False,unique=True)
    def __repr__(self):
        return "Item{}".format(self.name)