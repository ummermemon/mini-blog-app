from flask import Flask
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def test():
        return 'Project Setup'

    return app