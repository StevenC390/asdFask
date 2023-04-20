from datetime import datetime
from src.database import db, ma

class House(db.model):
    registration= db.Column(db.Integer,primary_key=True,nullable=False,autoincrement = True)
    adress      = db.Column(db.String,nullable=False)
    type        = db.Column(db.Integer,nullable=False)
    floor_count = db.Column(db.Integer)
    created_at  = db.Column(db.DateTime,default=datetime.now())
    updated_at  = db.Column(db.DateTime,onupdate=datetime.now())
    user_id     = db.Column(db.String(10),db.ForeignKey('user.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    
    def __init__(self, **fields):
        super().__init_(**fields)
        
    def __repr__ (self) -> str:
        return f"House >>> {self.name}"
    
class HouseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # fields =()
        model = House
        iclude_fk = True
        
house_schema = HouseSchema()
houses_schema = HouseSchema(many=True)