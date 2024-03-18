from dataclasses import dataclass
from datetime import datetime, time, date, timedelta

@dataclass
class Task:
    task_name:str = ''
    task_description:str = ''
    due_date:datetime = None

    def status(self):
        if self.due_date > datetime.now():
            return 'Pending'
        else:
            return 'Completed'

@dataclass
class Homework(Task):
    def __init__(self, task_name='', task_description='', due_date=None, subject=''):
        Task.__init__(self, task_name, task_description, due_date)
        self.subject = subject
        self.__task_status = None

    def status(self):
        delta = self.due_date - datetime.now()
        if delta > timedelta(days=14):
            self.__task_status = 'Not started'
        elif delta <= timedelta(days=14) and delta > timedelta(days=0):
            self.__task_status = 'In progress'
        elif delta <= timedelta(days=0):
            self.__task_status = 'Completed'
        else:
            self.__task_status = 'Invalid'
        return self.__task_status

@dataclass
class Meeting(Task):
    location:str = ''

    def status(self):
        if self.due_date > datetime.now():
            return 'Scheduled'
        else:
            return 'Happened'


homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2024,3, 13), "Math")
meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2024,9, 20), "Office A")

print("Homework:")
print("Task Name:", homework.task_name)
print("Task Description:", homework.task_description)
print("Due Date:", homework.due_date)
print("Subject:", homework.subject)
print("Status:", homework.status())
print("\n")
print("Meeting:")
print("Task Name:", meeting.task_name)
print("Task Description:", meeting.task_description)
print("Due Date:", meeting.due_date)
print("Location:", meeting.location)
print("Status:", meeting.status())
