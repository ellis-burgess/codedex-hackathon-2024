from flask import Flask, render_template, url_for
from boardgame_site import app
from boardgame_site.models import Event

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
  events = Event.query.all()
  return render_template('events_calendar.html', title='Events Calendar', events=events)

@app.route('/menu')
def menu():
  return render_template('menu.html', title='Menu')