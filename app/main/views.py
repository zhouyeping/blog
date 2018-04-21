from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from . import main
from app.service.BlogService import BlogService


@main.route('/')
def index():
    blog_service = BlogService()
    all_blog = blog_service.get_blog()
    return render_template('index.html', all_blog=all_blog)


@main.route('/blog/<blog_id>')
def blog(blog_id):
    blog_service = BlogService()
    a_blog = blog_service.get_blog_bid(blog_id)
    return render_template('blog_detail.html', blog=a_blog)


@main.route('/blog/add', methods=['GET'])
def add_blog_get():
    return render_template('blog_addition.html')


@main.route('/blog/add', methods=['POST'])
def add_blog_post():
    blog_service = BlogService()
    title = request.form.get('title')
    content = request.form.get('content')
    blog_service.add_blog(title=title, content=content)
    return redirect('/')


@main.route('/blog/update', methods=['POST'])
def update_blog():
    blog_service = BlogService()
    id = request.form.get('id')
    title = request.form.get('title')
    content = request.form.get('content')
    blog_service.update_blog(id, title, content)
    return redirect('/blog/' + str(id))


