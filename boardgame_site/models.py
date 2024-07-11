from datetime import datetime
from boardgame_site import db

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime, nullable=False)
  duration = db.Column(db.DateTime, nullable=False)
  recurring = db.Column(db.Boolean, nullable=False, default=False, server_default='0')
  frequency = db.Column(db.Text)
  end_recurrence = db.Column(db.DateTime)
  title = db.Column(db.Text, nullable=False)
  description = db.Column(db.Text, nullable=False)
  event_banner = db.Column(db.String(40), nullable=False, default='default.jpg', server_default='default.jpg')

  def __repr__(self):
    return_str = [f"Event: "]
    return_str.append(f"'{self.date}'")
    if self.recurring == True:
      return_str.append("(recurring event)")
      return_str.append(f"'{self.frequency}'")
      return_str.append(f"Ends: '{self.end_recurrence}'")
    return_str.append(f"'{self.title}'")
    return_str.append(f"'{self.description}'")
    return ' '.join(return_str)