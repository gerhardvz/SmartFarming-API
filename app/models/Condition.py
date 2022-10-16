from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from ..database import db, ma


class PlantCondition(db.Model):
    __tablename__ = "plant_condition"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    plant_id = Column(db.Integer, ForeignKey("plant.id"))


class PlantConditionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlantCondition
        sqla_session = db.session
        load_instance = True
