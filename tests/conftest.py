import pytest
from sqlalchemy import delete
from werkzeug.security import generate_password_hash
from website.__init__ import create_app
from website.__init__ import db
from website.auth import register, User

from website.auth import User
from main import app

@pytest.fixture(scope="session")
def flask_app():
    app = create_app()
    
    client = app.test_client()
    
    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()
    



@pytest.fixture(scope="session")
def app_db(flask_app):
    db.create_all()
    
    yield flask_app
    
    db.session.commit()
    db.drop_all
    
@pytest.fixture
def app_data(app_db):
    userx = register()
    userx.email = "rthu@gmail.com"
    userx.name = "arty"
    userx.password = generate_password_hash("passwordd")
    userx.password2 = generate_password_hash("passwordd")

    db.session.add(userx)
    
    db.session.commit()
    
    yield app_db
    
    db.session.execute(delete(User))
    db.session.commit()