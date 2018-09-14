from app.models import Site
from app import db

db.create_all()


def add_url(url):
    site = Site(
        url['url'],
        url['title'],
        url['keywords'],
        url['description']
    )
    db.session.add(site)
    db.session.commit()


def list_of_url():
    return Site.query.all()


def search(url):
    missing = Site.query.filter_by(url=url).first()
    return missing is None