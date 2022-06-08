import random
from datetime import datetime as dt

names = ['RENE', 'ASTRID', 'ANDRES', 'JAMES', 'ROBERT', 'JOHN', 'MARY', 'PATRICIA', 'JENNIFER', 'ANA']
days_week = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
date_format = "%H:%M"
employees = ''

def generate_schedule():
  hours_work = []
  pick_days = []
  pair_hours_work = []
  list_schedule = []
  schedule = ''

  random_number = random.randint(3, 5)

  for i in range(random_number*2):
    hours = dt(2020, 1, 1, random.randint(8, 21), random.randint(0, 59), 0, 0)
    formatted_hours = hours.strftime(date_format)
    hours_work.append(formatted_hours)

  hours_work = sorted(hours_work)

  pick_days = sorted(random.sample(days_week, random_number), key=days_week.index)

  for i in range (0, len(hours_work), 2):
    pair_hours_work.append([hours_work[i], hours_work[i+1]])

  for i in range(len(pair_hours_work)):
    list_schedule.append(f"{pick_days[i]}{pair_hours_work[i][0]}-{pair_hours_work[i][1]}")

  schedule = (',').join(list_schedule)

  return schedule

def generate_turns(names):
  employee_turns = []

  for name in names:
    employee_turns.append(f"{name}={generate_schedule()}")

  return employee_turns

employees = generate_turns(names)
