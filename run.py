import app
from app.services.MachineLearningService import ResNet9
if __name__ == '__main__':
    app = app.create_app()
    app.run()
