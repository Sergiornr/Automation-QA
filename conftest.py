
import pytest

@pytest.fixture
def posts_data():
    return {
        "title":"Mi primer posteo",
        "body": "contenido referente a mi primer posteo",
        "userId": 1
    }

@pytest.fixture
def users_data():
    return {
        "name":" Sergio Sanabria"
        "username": "Rene"
        "email": "rene@gmail.com"
    }