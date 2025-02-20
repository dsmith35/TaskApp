from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from os import path, getenv
import os

db = SQLAlchemy()
DB_NAME = "database.db"
TEST_DB_NAME="test-database.db"
# initialize db
def create_app(testing=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    if testing: 
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{TEST_DB_NAME}'
    db.init_app(app)

    is_vercel = getenv('VERCEL') == '1'

    # Set database path
    if is_vercel:
        # Use writable /tmp directory on Vercel
        db_path = os.path.join('/tmp', DB_NAME if not testing else TEST_DB_NAME)
    else:
        # Local development: place DB in instance folder
        db_folder = path.join(app.instance_path)
        os.makedirs(db_folder, exist_ok=True)
        db_path = path.join(db_folder, DB_NAME if not testing else TEST_DB_NAME)

    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Task, Project
        
    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


