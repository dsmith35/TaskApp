import pytest
from website.auth import User, register
from marshmallow import ValidationError



@pytest.mark.parametrize(
    "email, name, password1, password2, valid",
    [
        ("a", "danny", "jimmybob", "jimmybob", False),
        ("rthu@gmail.com", "arty", "passwordd", "passwordd", True)
    ]

    
)


def test_register(email, name, password1, password2, valid):
    schema = register()
    data = {
        "email": email,
        "name": name,
        "password1": password1,
        "password2": password2

    }
    try:
        userx = schema.load(data)
        assert valid
        
        assert userx is not None
        assert userx.email == email
        assert userx.name == name
        assert userx.password1 == password1
        assert userx.password2 == password2   
    except ValidationError:
        assert not valid