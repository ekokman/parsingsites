from flask import render_template, flash, redirect
from app import app
from forms import ParsingForm
from bs4 import BeautifulSoup
import urllib.request


def parsed_url(url):
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
    sites = [  # список сайтов
        {
            'url': 'https://translate.yandex.ru/',
            'title': 'Яндекс.Переводчик – словарь и онлайн перевод на английский, русский, немецкий, французский, украинский и другие языки.',
            'keywords': 'перевод, переводчик, перевод онлайн, переводчик онлайн, translate, англо-русский, машинный перевод"',
            'description': 'Перевод с английского, немецкого, французского, испанского, польского, турецкого и других языков на русский и обратно. Возможность переводить отдельные слова и фразы, а также целые тексты и в'
        }
    ]
    count_sites = len(sites)
    return render_template("index.html",
                           title="Main",
                           sites=sites,
                           count_sites=count_sites
                           )

@app.route('/parsing', methods = ['GET', 'POST'])
def parsing():
    form = ParsingForm()
    if form.validate_on_submit():
        return redirect('/parsed')
    return render_template('parsing.html',
                           title='Parsing',
                           form=form
                           )

@app.route('/parsed', methods = ['GET'])
def parsed():

    url = 'https://habr.com/post/193242/'
    url2 = 'https://translate.yandex.ru/'
    return render_template('parsed.html',
                           title='Parsed',
                           page=parsed_url(url2)
                           )

