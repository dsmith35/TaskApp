
import pytest
from website.models import User, Project
from marshmallow import ValidationError
import datetime




@pytest.mark.parametrize("email, name, password1, password2",[
    ("test@test.com", "testguy", "123456", "123456"),
    ("", "testguy", "123456", "123456")
])

def test_register(email, name, password1, password2):
    assert email == "test@test.com"
    assert password1 == password2
    assert email != ""
    
        