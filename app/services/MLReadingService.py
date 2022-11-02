import datetime
import numbers
import string
import time
import distutils

from flask import request
from sqlalchemy import asc, desc

from ..database import db

from app.models.Condition import PlantCondition, PlantConditionSchema
from app.models.Devices import Device, DeviceSchema
from app.models.ML_Reading import MlReading
from app.models.Plant import Plant
from app.models.Prediction_Enum import PredictionEnum
from app.models.Reading import Reading, ReadingSchema
from app.services import MachineLearningService


def add_new_ml_reading():
    reading_id = request.args.get('reading_id')
    device_id = request.args.get('device_id')
    img = request.files['image']

    # if reading_id is None:
    #     return "No reading_id Specified", 400
    if img is None:
        return "No image uploaded", 400
    # Test if reading Exists


    if reading_id is None:
        # Throw error if reading does not exists
        # raise Exception("The reading selected does not exist.")
        reading = Reading(timestamp=datetime.datetime.now(),device_id=device_id)

        db.session.add(reading)


    confidence, index = MachineLearningService.get_prediction(img.read())
    print(index)
    plant_condition = PlantCondition.query.join(Plant).filter(PlantCondition.id == index).one_or_none()
    plant_conditionSchema = PlantConditionSchema(many=False)
    plant = Plant.query.join(PlantCondition).filter(PlantCondition.id == index).one_or_none()
    print(plant.name)

    MLreading = MlReading( prediction=plant_condition.id, accuracy=confidence,reading_id=reading_id)
    # MlReading.add(MLreading)
    db.session.add(MLreading)
    db.session.commit()
    return { 'prediction':{'confidence_level':confidence,'Plant':plant.name,'Condition':plant_condition.name}}


def get_ml_readings_by_reading():
    data = request.get_json()
    reading_id = request.args.get('reading_id')
    ascending = bool(distutils.util.strtobool(request.args.get('ascending')))
    if reading_id is None:
        return "No reading_id Specified", 400
    if ascending is None:
        ascending = True

    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    if not isinstance(reading_id, int):
        raise ValueError(f"Timestamp value invalid: {reading_id}")
    return (MlReading.query
            .join(Reading)
            .join(PredictionEnum)
            .filter(Reading.id == reading_id)
            )
