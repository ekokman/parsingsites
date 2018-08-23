from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class ParsingForm(Form):
    url_of_site = TextField('url_of_site', validators=[Required()])
