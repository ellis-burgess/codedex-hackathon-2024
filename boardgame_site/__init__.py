from flask import Flask, url_for
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my top secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'events.db')

db = SQLAlchemy(app)

# Pages to include in the nav bar
def get_navaddresses():
  with app.app_context():
    return [
      {'name': 'Home', 'url': url_for('index')},
      {'name': 'About', 'url': url_for('about')},
      {'name': 'Reservations', 'url': url_for('reservations')},
      {'name': 'Events', 'url': url_for('events')},
      {'name': 'Menu', 'url': url_for('menu')}
    ]
    
# Context processor to make navaddresses available globally
@app.context_processor
def inject_navaddresses():
  return dict(navaddresses=get_navaddresses())

from boardgame_site import routes