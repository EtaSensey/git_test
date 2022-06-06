import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt





db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHERMY_DATABASE_URI'] = 'swlite:///test.db'
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    bcrypt.init_app(app)



    from blog.main.routes import main
    from blog.user.routes import users
    
    # Регистрация блюпринта
    app.register_blueprint(main)
    app.register_blueprint(users)
    
    return app
