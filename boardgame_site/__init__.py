from flask import Flask, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my top secret key'

# Pages to include in the nav bar
def get_navaddresses():
  with app.app_context():
    return [
      {'name': 'Home', 'url': url_for('index')},
      {'name': 'About', 'url': url_for('about')},
    ]
    
# Context processor to make navaddresses available globally
@app.context_processor
def inject_navaddresses():
  return dict(navaddresses=get_navaddresses())

from boardgame_site import routes