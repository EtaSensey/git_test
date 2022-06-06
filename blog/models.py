from flask_login import UserMixin
from blog import db




# Описание модели  User

class User(db.Model, UserMixin):
    
    
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(1020), unique=True, nullable=False) 
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg') 
    password = db.Column(db.String(60), nullable=False) 
    post = db.relationship('Post', backref='author', lazy=True)   # отношение между таблицей юзер и постом
        
    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.password})'