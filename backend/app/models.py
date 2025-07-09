from .extensions import db

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    author = db.Column(db.String(100))
    chapters = db.relationship("Chapter", backref="story", lazy=True)
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

