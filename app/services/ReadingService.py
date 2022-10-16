import datetime
import numbers
import string
import time
import distutils

from flask import request
from sqlalchemy import asc, desc

from app.models.Devices import Device, DeviceSchema
from app.models.ML_Reading import MlReading
from app.models.Prediction_Enum import PredictionEnum
from app.models.Reading import Reading, ReadingSchema


def get_readings():
    device_id = request.args.get('device_id')
    timestamp = request.args.get('timestamp')
    ascending = bool(distutils.util.strtobool(request.args.get('ascending')))

    # if device_id is None:
    #     return "No device_id Specified", 400
    # if timestamp is None:
    #     return "No timestamp Specified", 400
    # if ascending is None:
    #     ascending = True

    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    direction = asc if ascending else desc
    query = Reading.query
    if isinstance(device_id, int):
        query = query.join(Device).filter(Device.id == device_id)
    if isinstance(timestamp, str):
        # convert string Timestamp to unix timestamp
        date_format = datetime.datetime.strptime(timestamp,
                                                 "%Y-%m-%d %H:%M:%S")
        unix_time = datetime.datetime.timestamp(date_format)
        query = query.filter(Reading.timestamp == unix_time)
    query = query.order_by(direction("id")).all()
    reading_schema = ReadingSchema(many=True)
    return reading_schema.dump(query)


def add_new_reading(reading):
    if reading is None:
        return "No Reading Specified", 400

        # Test if device Exists
    db_reading = (Reading.query
                  .filter(Reading.timestamp == reading.timestamp)
                  .filter(Reading.device_id == reading.device_id)
                  .one_or_none()
                  )
    if db_reading is not None:
        # return reading if reading does  exists
        return db_reading, 200
        # return ("The timestamp already exist.")
    # Test if device Exists
    device = (Device.query
              .filter(Device.id == reading.device_id)
              .one_or_none()
              )
    if device is None:
        # Throw error if device does not exists
        return "The device selected does not exist.", 400
    # Test if timestamp is not in the future
    if reading.timestamp <= int(time.time()):
        Reading.add(reading)
        reading = (Reading.query
                   .filter(Reading.timestamp == reading.timestamp)
                   .filter(Reading.device_id == reading.device_id)
                   .one_or_none()
                   )
        return reading, 201

    return ("Timestamp can not be in the future."), 400


def get_reading_by_id(id):
    ascending = bool(distutils.util.strtobool(request.args.get('ascending')))
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    direction = asc if ascending else desc
    query = (Reading.query
             .filter(Reading.id == id)
             .order_by(direction("id"))
             .all())

    reading_schema = ReadingSchema(many=False)
    return reading_schema.dump(query)


def get_readings_by_device_id(device_id, ascending):
    # data = request.get_json()
    # device_id = request.args.get('device_id')
    # ascending = bool(distutils.util.strtobool(request.args.get('ascending')))
    if device_id is None:
        return "No device_id Specified", 400
    if ascending is None:
        ascending = True
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    if not isinstance(device_id, int):
        raise ValueError(f"Device value invalid: {device_id}")
    direction = asc if ascending else desc
    query = (Reading.query
             .join(Device)
             .filter(Device.id == device_id)
             )
    query = query.order_by(direction("id")).all()
    reading_schema = ReadingSchema(many=True)
    return reading_schema.dump(query)


def get_readings_by_timestamp():
    timestamp = request.args.get('timestamp')
    ascending = bool(distutils.util.strtobool(request.args.get('ascending')))
    if timestamp is None:
        return "No timestamp Specified", 400
    if ascending is None:
        ascending = True
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    if not isinstance(timestamp, int):
        raise ValueError(f"Timestamp value invalid: {timestamp}")
    return (Reading.query
            .filter(Reading.timestamp == timestamp)
            )


def remove_reading():
    reading_id = request.args.get('reading_id')
    reading = (Reading.query
               .filter(Reading.id == reading_id)
               .one_or_none())
    Reading.remove(reading)
    return True, 200
