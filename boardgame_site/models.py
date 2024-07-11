from datetime import datetime
from boardgame_site import db

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False)
  duration = db.Column(db.DateTime, nullable=False)
  recurring = db.Column(db.Boolean, nullable=False, default=False)
  frequency = db.Column(db.Text)
  end_recurrence = db.Column(db.DateTime)
  title = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)
  event_banner = db.Column(db.String(40), nullable=False, default='default.jpg')