import pytest
from website.models import User, Project
from marshmallow import ValidationError
import datetime

# start_date = datetime.datetime.strptime("2023-11-20 01-01-01", "%Y-%m-%d %H-%m-%s")
# deadline = datetime.datetime.strptime("2023-12-20 01-01-01", "%Y-%m-%d %H-%m-%s")

bdata = {"name": "Johnn", "sdate": "2023-11-20", "deadline": "2023-12-20", "description": "327FinalAsssignment" }

@pytest.mark.parametrize("name, sdate, deadline, description",[
    ("Johnn", "2023-11-20", "2023-12-20", "327FinalAsssignment" ),
    ("Johnn", "2023-12-20", "2023-11-20", "327FinalAsssignment" ),
    ("Johnn", "", "2023-11-20", "327FinalAsssignment" ),
    ("Johnn", "2023-12-20", "", "327FinalAsssignment" )
    
    
])
#def test_newproject(client, app):
#    response = client.post("/newproject", data = bdata)
#    with app.app_context():
#        assert bdata["name"] == "Johnn"
#        assert bdata["description"] == "327FinalAsssignment"
#        assert bdata["sdate"] < bdata["deadline"]
#        assert bdata["sdate"] != ""
#        assert bdata["deadline"] != ""      
def test_newproject(name, sdate, deadline, description):
    assert name == "Johnn"
    assert description == "327FinalAsssignment"
    assert sdate < deadline
    assert sdate != ""
    assert deadline != ""

