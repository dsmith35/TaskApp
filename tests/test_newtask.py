
import pytest
from website.models import User, Project
from marshmallow import ValidationError
import datetime




@pytest.mark.parametrize("assignee, sdate, deadline, description",[
    ("Johnn", "2023-11-20", "2023-12-20", "327Asssignment" ),
    ("Johnn", "2023-12-20", "2023-11-20", "327Asssignment" ),
    ("Johnn", "", "2023-11-20", "327Asssignment" ),
    ("Johnn", "2023-12-20", "", "327Asssignment" )
])

def test_newtask(assignee, sdate, deadline, description):
    assert assignee == "Johnn"
    assert description == "327Asssignment"
    assert sdate < deadline
    assert sdate != ""
    assert deadline != ""