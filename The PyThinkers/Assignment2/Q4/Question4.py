from dataclasses import dataclass
from datetime import datetime, date, time, timedelta

@dataclass
class Event:
    name:str = ''
    location:str = ''
    start_date:datetime = None
    end_date:datetime = None

    def duration(self):
        diff = self.end_date - self.start_date
        return diff.days

@dataclass
class Conference(Event):
    attendees:int = 0

    def duration(self):
        diff = (self.end_date - self.start_date)
        hours = diff.days * 24
        hours2 = (f'{diff:%H}')
        hours = hours + hours2
        print(diff)
        return hours

event = Event("Birthday Party", "New York", datetime(2023, 8, 25),
                                            datetime(2024, 8, 26))
conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9,15, 3),
                                                    datetime(2023, 9, 17), 500)

print("Event:")
print("Name:", event.name)
print("Location:", event.location)
print("Start Date:", event.start_date)
print("End Date:", event.end_date)
print("Duration (days):", event.duration())
print("\n")
print("Conference:")
print("Name:", conference.name)
print("Location:", conference.location)
print("Start Date:", conference.start_date)
print("End Date:", conference.end_date)
print("Attendees:", conference.attendees)
print("Duration (hours):", conference.duration())

