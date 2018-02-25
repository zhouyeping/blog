from . import db


class Blog(db.Model):
    __tablename = 'blog'
    blog_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(65536), nullable=False)
    add_time = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, title, content, add_time):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.add_time = add_time


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Tag(db.Model):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, tag_name):
        self.tag_name = tag_name


class BlogTagRelation(db.Model):
    __tablename__ = 'blog_tag_relation'
    r_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, nullable=False)
    blog_id = db.Column(db.Integer, nullable=False)

