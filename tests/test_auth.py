import pytest
from website.models import User
from marshmallow import ValidationError



data1 = {"email":"test@test.com","name":"testguy","password1":"123456","password2":"123456"}

def test_register(client, app):
    response = client.post("/register", data=data1)
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"