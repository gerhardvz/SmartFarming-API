import connexion

from flasgger import Swagger, LazyString, LazyJSONEncoder




from app import conf


def create_app():



    # app = Flask(__name__)
    connex_app = connexion.FlaskApp(__name__, specification_dir='./')
    app = connex_app.app
    app.json_encoder = LazyJSONEncoder
    conf.setConfig(app)


    from . import database
    database.setDB(app)

    from . import models, routes, services
    connex_app.add_api('swagger.yml',
                       base_path='{url_prefix}'.format(url_prefix=app.config.get('URL_PREFIX', '/api')),
                       )
    # models.init_app(app)
    routes.init_app(app)
    # services.init_app(app)
    from .services import MachineLearningService
    MachineLearningService.init()
    return connex_app

# for moving data into GPU (if available)
