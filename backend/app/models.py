from .extensions import db
from datetime import datetime

story_categories = db.Table(
    'story_categories',
    db.Column('story_id', db.Integer, db.ForeignKey('story.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    author = db.Column(db.String(100))
    url_image = db.Column(db.String(255))
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    chapters = db.relationship("Chapter", backref="story", lazy=True)
    
    # Quan hệ nhiều-nhiều với Category
    categories = db.relationship('Category', secondary=story_categories, backref='stories', lazy='subquery')

    def __init__(self, title, description, author):
        self.title = title  
        self.description = description
        self.author = author

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    story_id = db.Column(db.Integer, db.ForeignKey("story.id"), nullable=False)
    def __init__(self, title, content, story_id):
        self.title = title
        self.content = content
        self.story_id = story_id

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name