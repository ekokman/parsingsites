from app.models import Sites
from app import db

db.create_all()


def add_url(url):
    site = Sites(
        url['url'],
        url['title'],
        url['keywords'],
        url['description']
    )
    db.session.add(site)
    db.session.commit()


def list_of_url():
    return Sites.query.all()


def search(url):
    missing = Sites.query.filter_by(url=url).first()
    return missing is None