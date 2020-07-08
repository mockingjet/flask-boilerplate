import sys
sys.dont_write_bytecode = True

import pytest

from jetblog.app import create_app
from jetblog.settings import TestConfig
from jetblog.database import engine, db_session, Base


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    ctx = app.test_request_context()
    ctx.push()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield app

    db_session.remove()
    Base.metadata.drop_all(engine)
    ctx.pop()


@pytest.fixture()
def client(app):
    return app.test_client()
