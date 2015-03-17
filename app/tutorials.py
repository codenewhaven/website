from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound

tutorials = Blueprint('tutorials',
                      __name__,
                      template_folder='templates')

@tutorials.route('/')
def tutorials_home():
    print 'all tutorials:'
    print all_tutorials()
    return render_template('pages/tutorials.html')
