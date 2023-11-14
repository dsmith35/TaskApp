import pytest
from sqlalchemy import delete
from werkzeug.security import generate_password_hash
from website.__init__ import create_app
from website.__init__ import db
from website.auth import register, User

from website.auth import User
from main import app

@pytest.fixture()
def app():
    app = create_app()

    with app.app_context():
        db.create_all()
    yield app
    # code here gets run after pytest finishes running
    ###
    



@pytest.fixture()
def app_db(flask_app):
    db.create_all()
    
    yield flask_app
    
@pytest.fixture()
def client(app):
    return app.test_client()


# @pytest.fixture
# def app_data(app_db):
#     userx = register()
#     userx.email = "rthu@gmail.com"
#     userx.name = "arty"
#     userx.password = generate_password_hash("passwordd")
#     userx.password2 = generate_password_hash("passwordd")

#     db.session.add(userx)
    
#     db.session.commit()
    
#     yield app_db
    
#     db.session.execute(delete(User))
#     db.session.commit()