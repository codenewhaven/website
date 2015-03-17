import os
from flask import Flask, g
from app.website import website
from app.tutorials import tutorials
from app import errors

from tutorials import Tutorial, all_tutorials


# Global app object
app = Flask(__name__)

# List of Tutorial objects
all_tuts = all_tutorials(os.path.join(os.getcwd(), 'tutorials'))
app.config['all_tuts'] = all_tuts

# Basic website
app.register_blueprint(website, static_folder='../static/')

# Tutorials section of website
app.register_blueprint(
    tutorials, url_prefix='/tutorials', static_folder='../static/')

# Http error views (404, 503, etc.)
errors.init_errors(app)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
