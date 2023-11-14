

import pytest
from website.models import User, Project
from marshmallow import ValidationError
import datetime




@pytest.mark.parametrize("email, password",[
    ("rthu@gmail.com", "ILOVE327"),
    ("", "ILOVE327")

])


def test_login(email, password):
    assert email == "rthu@gmail.com"
    assert password == "ILOVE327"
    assert password != ""