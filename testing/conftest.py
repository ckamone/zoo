"""
info
:return:
"""

import pytest
from flask.testing import FlaskClient

from ..app import app


@pytest.fixture
def client() -> FlaskClient:
    """
    info
    :return:
    """
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
