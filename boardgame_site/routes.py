from flask import Flask, render_template, url_for
from boardgame_site import app

@app.route('/')
def index():
  return render_template('index.html', title='Home')

@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/reservations')
def reservations():
  return render_template('reservations.html', title='Reservations')

@app.route('/events')
def events():
  return render_template('events_calendar.html', title='Events Calendar')

@app.route('/menu')
def menu():
  return render_template('menu.html', title='Menu')