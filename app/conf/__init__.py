import os


def setConfig(app):
    basedir=os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'PRJ381-SmartFarming.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SWAGGER'] = {
    #     'title': 'My API',
    #     'uiversion': 3,
    #     "specs_route": "/swagger/"
    # }