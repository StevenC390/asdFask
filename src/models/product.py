from datetime import datetime
from src.database import db, ma
from sqlalchemy.orm import validates
import re

class Product(db.model):
    code        = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement = True)
    name        = db.Column(db.String(50),unique=True,nullable=False)
    price       = db.Column(db.Float,nullable=False)
    expiration  = db.Column(db.DateTime,default=datetime.year(2025),nullable=True)
    created_at  = db.Column(db.DateTime,default=datetime.now())
    updated_at  = db.Column(db.DateTime,onupdate=datetime.now())
    user_id     = db.Column(db.String(10),db.ForeignKey('user.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    
    def __init__(self, **fields):
        super().__init_(**fields)
        
    def __repr__ (self) -> str:
        return f"Product >>> {self.name}"
    
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise AssertionError('No name provided')
        if not value.isalnum():
            raise AssertionError('Name value must be alphanumeric')
        if len(value) < 5 or len(value) > 50:
            raise AssertionError('Name must be between 5 and 50 characters')
        if Product.query.filter(Product.name == value).first():
            raise AssertionError('Name is already in use')
        return value
    @validates('price')
    def validate_price(self, key, value):
        if not value:
            raise AssertionError('No price provided')
            # re.match(r"\d+\.*\d*", str)
        if not re.compile("^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$", value):
            raise AssertionError('Price value must be a real number')
        if value < 0:
            raise AssertionError('Price must be above greater or equal to $0')
        return value
    @validates('expiration')
    def validate_expiration(self, key, value):
        # This field is not mandatory!
        if not value:
            raise value
        if not re.match("[0-9]{1,2}\\-[0-9]{1,2}\\-[0-9]{4}", value):
            raise AssertionError('Provided date is not a real date value')
        today = datetime.datetime.now()
        expiration = datetime.datetime.strptime(value, "%Y-%m-%d")
        if not expiration >= today:
            raise AssertionError('Expiration date must be today or later')
        return value
            
            
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # fields =()
        model = Product
        iclude_fk = True
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)