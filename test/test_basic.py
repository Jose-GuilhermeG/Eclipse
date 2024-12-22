from pytest import fixture
from app import create_app

@fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client
