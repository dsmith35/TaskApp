import pytest
from website.models import User, Project
from marshmallow import ValidationError
import datetime

# start_date = datetime.datetime.strptime("2023-11-20 01-01-01", "%Y-%m-%d %H-%m-%s")
# deadline = datetime.datetime.strptime("2023-12-20 01-01-01", "%Y-%m-%d %H-%m-%s")
data1 = {"email":"test@test.com","name":"testguy","password1":"123456","password2":"123456"}
bdata = {"name": "Johnn", "sdate": "2023-11-20", "deadline": "2023-12-20", "description": "327FinalAsssignment" }



def test_register(client, app):
    response = client.post("/register", data=data1)
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"
        

def test_newproject(client, app):
    response = client.post("/newproject", data = bdata)
    with app.app_context():
        assert bdata["name"] == "Johnn"
        assert bdata["description"] == "327FinalAsssignment"
        assert bdata["sdate"] < bdata["deadline"]
        