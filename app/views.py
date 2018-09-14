from flask import render_template, request, flash
from bs4 import BeautifulSoup

import urllib.request
import validators

from app import app
from app.models import Site


def parsing_url(url):
    page = urllib.request.urlopen(url)
    html = BeautifulSoup(page.read(), "html.parser")
    title, keywords, description = None, None, None

    title = html.title.string

    for tags in html.find_all('meta'):
        if tags.get('name') == 'keywords':
            keywords = tags.get('content')
        if tags.get('name') == 'description':
            description = tags.get('content')

    meta = {'url': url,
            'title': title,
            'keywords': keywords,
            'description': description
            }
    return meta


@app.route('/')
def index():
    site = Site(1, 2, 3, 4)
    parsed_sites = site.list_of_full()
    return render_template("index.html",
                           title="Main",
                           sites=parsed_sites,
                           count_sites=len(parsed_sites)
                           )

@app.route('/parsing/')
def parsing():
    return render_template('parsing.html', title="Parsing")


@app.route('/parsed/', methods=['POST'])
def parsed():
    error = None
    url = request.form['url']
    parsed_url = parsing_url(url)
    site = Site(
        parsed_url['url'],
        parsed_url['title'],
        parsed_url['keywords'],
        parsed_url['description']
    )
    if validators.url(url) is not True:
        error = "Not a valid URL"
    elif site.search(url) == False:
        error = 'The URL is already in the database'
        parsed_url = None
    else:

        site.add_url()
    flash(error)
    return render_template('parsed.html',
                           url=url,
                           parsed_url=parsed_url,
                           title="Parsed",
                           error=error
                           )