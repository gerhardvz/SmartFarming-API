from sqlalchemy import Column, Integer, String, ForeignKey, Table, Numeric
from ..database import db, ma


class MlReading(db.Model):
    __tablename__ = "ml_reading"
    id = Column(Integer, primary_key=True)
    prediction = Column(Integer, ForeignKey("plant_condition.id"))
    accuracy = Column(Numeric)
    reading_id = Column(Integer, ForeignKey("reading.id"))


class ReadingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MlReading
        sqla_session = db.session
        load_instance = True
