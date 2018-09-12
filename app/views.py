from flask import render_template, redirect, request, flash
from app import app
from bs4 import BeautifulSoup
from app.db import add_url, list_of_url, search
import urllib.request
import validators


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
@app.route('/index')
def index():
    parsed_sites = list_of_url()
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
    parsed_url = None
    if validators.url(url) is not True:
        error = "Not a valid URL"
    elif search(url) == False:
        error = 'The URL is already in the database'
    else:
        parsed_url = parsing_url(url)
        add_url(parsed_url)
    flash(error)
    return render_template('parsed.html',
                           url=url,
                           parsed_url=parsed_url,
                           title="Parsed",
                           error=error
                           )