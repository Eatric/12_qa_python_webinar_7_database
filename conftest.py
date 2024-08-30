import pytest

from database import Database


@pytest.fixture(scope='package')
def database():
    connection = Database()

    return connection
