from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my top secret key'

from boardgame_site import routes