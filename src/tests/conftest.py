from typing import Generator

import pytest
from fastapi.testclient import TestClient

from blog_platform.app import app
from blog_platform.db.session import SessionLocal


@pytest.fixture(scope='session')
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app) as c:
        yield c

