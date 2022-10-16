from ..services.DeviceService import *
from flasgger import swag_from

def init_app(app):
    print(app)
    # @app.route('/devices')
    # def getDevices():
    #
    #     return get_device_by_id(ascending=True)
    #
    # @app.route('/devices')
    # def addDevice():
    #     print("Done")
    #     return add_device()
    #
    #
    # @app.route('/readings')
    # def getReadingByDeviceId():
    #     print("Reading")
    #     data = request.get_json()
    #     device_id = request.args.get('device_id')
    #     ascending = request.args.get('ascending')
    #     print("Reading")
    #     return get_readings_by_device_id(device_id,ascending )
    #
    # @app.route('/readings')
    # def getReadingByTimestamp():
    #
    #     print("Reading2")
    #     return get_readings_by_timestamp( )
    #
    # @app.route('/readings/:id')
    # def getReadingById(id):
    #     return get_ml_readings_by_reading( reading_id=id, ascending=True)
    #
    # @app.route('/readings/:id/ml')
    # def getMlReadingById(id):
    #     return get_ml_readings_by_reading( reading_id=id, ascending=True)
