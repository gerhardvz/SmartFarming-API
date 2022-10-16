from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from ..database import db, ma


class Reading(db.Model):
    __tablename__ = "reading"
    id = Column(Integer, primary_key=True)
    timestamp = Column(db.DateTime)
    device_id = Column(db.Integer, ForeignKey("device.id"))
    ml_readings = relationship("MlReading")


class ReadingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reading
        sqla_session = db.session
        load_instance = True
