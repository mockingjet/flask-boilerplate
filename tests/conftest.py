import sys
sys.dont_write_bytecode = True

import pytest

from jetblog.app import create_app
from jetblog.settings import TestConfig
from jetblog.database import Base, engine


@pytest.fixture(scope="class")
def app():
    app = create_app(TestConfig)
    ctx = app.test_request_context()
    ctx.push()
    Base.metadata.create_all(engine)

    yield app

    Base.metadata.drop_all(engine)
    ctx.pop()


@pytest.fixture(scope="class")
def client(app):
    return app.test_client()
