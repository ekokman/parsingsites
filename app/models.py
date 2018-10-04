from app import db

db.create_all()

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

    def add_url(self):
        db.session.add(self)
        db.session.commit()

    def list_of_full(self):
        return self.query.all()

    def search(self, url):
        missing = self.query.filter_by(url=url).first()
        return missing is None