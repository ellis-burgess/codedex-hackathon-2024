from flask import Flask, render_template, url_for, request, jsonify
from boardgame_site import app
from boardgame_site.models import Event
from datetime import datetime, timedelta
from .utils import get_events_for_week

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
  current_date = request.args.get('date')
  if current_date:
    start_date = datetime.strptime(current_date, '%Y-%m-%d')
  else:
    start_date = datetime.now() - timedelta(days=datetime.now().weekday())
  
  events = get_events_for_week(start_date)
  next_week = (start_date + timedelta(days=7)).strftime('%Y-%m-%d')
  prev_week = (start_date - timedelta(days=7)).strftime('%Y-%m-%d')
  
  return render_template('events_calendar.html', events=events, start_date=start_date, next_week=next_week, prev_week=prev_week, timedelta=timedelta, title="Events Calendar")

@app.route('/api/events')
def api_events():
  current_date = request.args.get('date')
  if current_date:
    start_date = datetime.strptime(current_date, '%Y-%m-%d')
  else:
    start_date = datetime.now() - timedelta(days=datetime.now().weekday())
  
  events = get_events_for_week(start_date)
  return jsonify(events)

@app.route('/menu')
def menu():
  return render_template('menu.html', title='Menu')