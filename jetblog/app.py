from flask import Flask

from . import commands
from .modules import articles
from .settings import DevConfig
from .database import db_session


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    register_bps(app)
    register_cmds(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app


def register_bps(app: Flask):
    app.register_blueprint(articles.views.bp, url_prefix="/api/v1")


def register_cmds(app: Flask):
    app.cli.add_command(commands.db)
    app.cli.add_command(commands.seed)
    app.cli.add_command(commands.make)
