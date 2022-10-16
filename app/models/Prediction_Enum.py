from sqlalchemy import Column, Integer, String, ForeignKey, Table, Numeric

from ..database import db, ma


class PredictionEnum(db.Model):
    __tablename__ = "prediction_enum"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class PredictionEnumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PredictionEnum
        sqla_session = db.session
        load_instance = True
