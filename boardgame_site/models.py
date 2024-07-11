from datetime import datetime
from boardgame_site import db
from sqlalchemy import text

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False)
  recurring = db.Column(db.Boolean, nullable=False, default=False, server_default=text('0'))
  frequency = db.Column(db.Text)
  end_recurrence = db.Column(db.DateTime)
  title = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)
  event_banner = db.Column(db.String(40), nullable=False, default='sipnplay.png', server_default='sipnplay.png')

  def __repr__(self):
    return_str = [f"Event: "]
    return_str.append(f"'{self.start_time}'")
    if self.recurring == True:
      return_str.append("(recurring event)")
      return_str.append(f"'{self.frequency}'")
      return_str.append(f"Ends: '{self.end_recurrence}'")
    return_str.append(f"'{self.title}'")
    return_str.append(f"'{self.description}'")
    return ' '.join(return_str)