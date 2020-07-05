import pytest

from jetblog.app import create_app
from jetblog.settings import TestConfig


@pytest.fixture(scope='session')
def app():
    return create_app(TestConfig)
