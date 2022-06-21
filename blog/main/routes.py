from flask import Flask, Blueprint, render_template, request, url_for
from flask_login import current_user, login_required
from jinja2 import TemplatesNotFound

from blog.models import Post


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    return render_template('main/index.html', title='Главная')

@main.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    post = Post.query.get(current_user.id)
    if post:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
        image_file = url_for('static', filename=f'profile_pics/{current_user.username}/{post.image_post}')

        return render_template('main/blog.html', title='Блог', posts=posts, image_file=image_file)
    else:
        return render_template('main/blog.html', title='Блог', nothing='Постов пока нет')

@main.route('/html_page')
def html_page():
    return render_template('main/html_page.html')

@main.route('/css_page')
def css_page():
    return render_template('main/css_page.html')

@main.route('/js_page')
def js_page():
    return render_template('main/js_page.html')

@main.route('/python_page')
def python_page():
    return render_template('main/python_page.html')

@main.route('/flask_page')
def flask_page():
    return render_template('main/flask_page.html')

@main.route('/django_page')
def django_page():
    return render_template('main/django_page.html')
