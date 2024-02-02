from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    from . import recordsearch
    app.register_blueprint(recordsearch.bp)
    app.secret_key='testing'

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello test!'

    return app
if __name__ == '__main__':
    app=create_app()
    app.run()