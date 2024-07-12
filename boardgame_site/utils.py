from datetime import datetime, timedelta
from .models import Event  # Ensure Event is correctly imported from your models

def get_events_for_week(start_date):
  events = Event.query.all()
  end_date = start_date + timedelta(days=7)
  
  week_events = []

  for event in events:
    # Add event if it falls within the current week
    if start_date <= event.start_time < end_date:
      event.formatted_start_time = event.start_time.strftime('%A, %B %d %Y at %I:%M %p')
      week_events.append(event)

    # Handle recurring events
    if event.recurring:
      recurrence_end_date = event.end_recurrence if event.end_recurrence else datetime.max
      event_date = event.start_time
      
      while event_date < end_date and event_date < recurrence_end_date:
        event_date = get_next_event_date(event_date, event.frequency)
        if start_date <= event_date < end_date:
          recurring_event = {
            'id': event.id,
            'title': event.title,
            'start_time': event_date,
            'formatted_start_time': event_date.strftime('%A, %B %d %Y at %I:%M %p'),
            'event_banner': event.event_banner,
            'description': event.description,
            'recurring': event.recurring,
            'frequency': event.frequency,
            'end_recurrence': event.end_recurrence
          }
          week_events.append(recurring_event)
  return week_events

def get_next_event_date(event_date, frequency):
  if frequency.lower() == 'daily':
    return event_date + timedelta(days=1)
  elif frequency.lower() == 'weekly':
    return event_date + timedelta(weeks=1)
  elif frequency.lower() == 'monthly':
    return event_date + timedelta(weeks=4)
  elif frequency.lower() == 'yearly':
    return event_date + timedelta(weeks=52)