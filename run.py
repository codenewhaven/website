from flask import Flask
from app.website import website
from app import errors

app = Flask(__name__)
app.register_blueprint(website, static_folder='../static/')

errors.init_errors(app)



if __name__ == '__main__':
    app.run(debug=True)
