from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound

website = Blueprint('website',
                    __name__,
                    template_folder='templates')


@website.route('/')
def home():
    return render_template('pages/home.html')


@website.route('/tutorials')
def tutorials():
    return render_template('pages/tutorials.html')


@website.route('/help')
def help():
    return render_template('pages/help.html')


@website.route('/contact')
def contact():
    return render_template('pages/contact.html')


@website.route('/about/')
@website.route('/about/<section>')
def about(section='mission'):
    try:
        return render_template("pages/about/%s.html" % section)
    except TemplateNotFound:
        abort(404)
