from flask import Flask, render_template, url_for
from boardgame_site import app

@app.route('/')
def index():
  return render_template('index.html', title='Home')

@app.route('/about')
def about():
  return render_template('about.html', title='About')