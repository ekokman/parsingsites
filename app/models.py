from app import db


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    title = db.Column(db.String())
    keywords = db.Column(db.String())
    description = db.Column(db.String())

    def __init__(self, url, title, keywords, description):
        self.url = url
        self.title = title
        self.keywords = keywords
        self.description = description