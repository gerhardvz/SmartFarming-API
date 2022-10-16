from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from ..database import db, ma


class Plant(db.Model):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # condition = relationship("Condition")


class PlantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plant
        sqla_session = db.session
        load_instance = True