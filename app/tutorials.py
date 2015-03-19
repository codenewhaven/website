from flask import Blueprint
from flask import g
from flask import render_template, abort
from flask import current_app
from jinja2 import TemplateNotFound


# from tutorial import all_tutorials()

tutorials = Blueprint('tutorials',
                      __name__,
                      template_folder='templates')


def register_tutorials():
    g.all_tuts = current_app.config.get('all_tuts')


tutorials.before_request(register_tutorials)


def find_tutorial(tutslug):
    for tut in g.all_tuts:
        if tut.slug == tutslug:
            return tut
    raise KeyError('Cannot find tutorial %s' % tutslug)

@tutorials.route('/')
def tutorials_home():
    return render_template('pages/tutorials.html')


@tutorials.route('/<tutslug>/')
@tutorials.route('/<tutslug>')
def tutorial(tutslug):
    try:
        return render_template("pages/tutorial.html",
                               tutorial=find_tutorial(tutslug))
    except TemplateNotFound:
        abort(404)
    except KeyError:
        print 'key error'
        abort(404)

@tutorials.route('/<tutslug>/view/<subdir>/<file_id>/')
@tutorials.route('/<tutslug>/view/<subdir>/<file_id>')
def tutorial_file(tutslug, subdir, file_id):
    try:
        tutorial = find_tutorial(tutslug)
        file = tutorial.find_file_by_id(subdir, file_id)


        return render_template("pages/tutorial_file.html",
                               tutslug=tutslug, file=file)
    except TemplateNotFound:
        abort(404)
