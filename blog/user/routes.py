from crypt import methods
import os
import shutil

from blog.models import User, db
from blog import bcrypt
from flask import Flask, Blueprint, flash, redirect, render_template, url_for
from blog.user.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)


# Маршрут для регистрации
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # Проверка валидации
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        # создания пути где будет папка с данными пользователя
        full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', user.username)
        # Если папки нет то зоздать
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        
        shutil.copy(f"{os.getcwd()}/blog/static/profile_pics/default.jpg", full_path)
        flash("Ваш акаунт был создан. Вы можете войти в блог", 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, title="Регистрация", legend="Регистрация")

@users.route('/login', methods=['GET', 'POST'])
def login():
    return "Hello"
