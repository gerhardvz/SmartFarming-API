from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from ..database import db, ma


class Plant(db.Model):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    scientific_name = Column(String)
    category = Column(String)
    max_light_mmol = Column(Integer)
    min_light_mmol = Column(Integer)
    max_light_lux = Column(Integer)
    min_light_lux = Column(Integer)
    max_temp = Column(Integer)
    min_temp = Column(Integer)
    max_env_humid = Column(Integer)
    min_env_humid = Column(Integer)
    max_soil_moist = Column(Integer)
    min_soil_moist = Column(Integer)
    max_soil_ec = Column(Integer)
    min_soil_ec = Column(Integer)
    url = Column(String)
    # condition = relationship("Condition")


class PlantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plant
        sqla_session = db.session
        load_instance = True