from sqlalchemy import Column, Integer, String, Table

from sqlalchemy.orm import relationship, backref

from ..database import db, ma


class Device(db.Model):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # readings = relationship("Reading")


class DeviceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        sqla_session = db.session
        load_instance = True
