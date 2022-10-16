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


def get_device():
    ascending=None
    if 'ascending' in request.args:
        ascending = bool(distutils.util.strtobool(request.args.get('ascending')))

    if ascending is None:
        ascending = True
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    direction = asc if ascending else desc
    devices = Device.query \
        .order_by(direction("id")) \
        .all()
    device_schema = DeviceSchema(many=True)
    return device_schema.dump(devices)

def get_device_by_id(id):

    ascending = bool(distutils.util.strtobool(request.args.get('ascending')))
    if ascending is None:
        ascending = True
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    direction = asc if ascending else desc
    devices = Device.query.filter(Device.id==id) \
        .order_by(direction("id")) \
        .all()
    device_schema = DeviceSchema(many=True)
    return device_schema.dump(devices)


def add_device(device):
    # device = request.args.get('name')
    if device is None:
        return "No device Specified", 400
    Device.add(device)
    print("Add Device " + ":" + request.args.get('name'))
    device_schema = DeviceSchema(many=False)
    return device_schema.dump(device)


def update_device(device):


    if device is None:
        return "No device Specified", 400

    device_update = Device.query.filter(Device.id == device.id)
    device_update.name = device.name

    Device.update(device_update)

    device_schema = DeviceSchema(many=False)
    return device_schema.dump(device)


def delete_device():
    device_id = request.args.get('device_id')
    device = Device.query.filter(Device.id == device_id)
    Device.remove(device)
    device_schema = DeviceSchema(many=False)
    return device_schema.dump(device)


