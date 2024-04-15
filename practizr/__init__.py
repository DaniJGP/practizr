import os

from flask import Flask

def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "practizr.sqlite")
    )

    app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db, auth, views
    
    db.init_app(app)
    app.register_blueprint(views.views_bp)
    app.register_blueprint(auth.auth_bp)

    return app