import datetime
import numbers
import string
import time
import distutils

from flask import request
from sqlalchemy import asc, desc

from app.models.Plant import PlantSchema, Plant



def get_plants():
    ascending=None
    if 'ascending' in request.args:
        ascending = bool(distutils.util.strtobool(request.args.get('ascending')))

    if ascending is None:
        ascending = True
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    direction = asc if ascending else desc
    devices = Plant.query \
        .order_by(direction("id")) \
        .all()
    device_schema = PlantSchema(many=True)
    return device_schema.dump(devices)

def get_plant_by_id(id):

    ascending = bool(distutils.util.strtobool(request.args.get('ascending')))
    if ascending is None:
        ascending = True
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")
    direction = asc if ascending else desc
    devices = Plant.query.filter(Plant.id==id) \
        .order_by(direction("id")) \
        .all()
    device_schema = PlantSchema(many=True)
    return device_schema.dump(devices)


def add_plant(plant):
    # device = request.args.get('name')
    if plant is None:
        return "No device Specified", 400
    Plant.add(plant)
    print("Add Device " + ":" + request.args.get('name'))
    device_schema = PlantSchema(many=False)
    return device_schema.dump(plant)


def delete_plant():
    plant_id = request.args.get('plant_id')
    device = Plant.query.filter(Plant.id == plant_id)
    Plant.remove(device)
    device_schema = PlantSchema(many=False)
    return device_schema.dump(device)


