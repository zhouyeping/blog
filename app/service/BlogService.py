from app.models import Blog
from app import db
from datetime import date


class BlogService:

    def __init__(self):
        pass

    def get_blog(self):
        return Blog.query.all()

    def get_blog_bid(self, id):
        return Blog.query.filter(Blog.blog_id == id).first()

    def add_blog(self, title, content):
        add_time = date.today()
        new_blog = Blog(1, title, content, add_time)
        db.session.add(new_blog)
        db.session.commit()
