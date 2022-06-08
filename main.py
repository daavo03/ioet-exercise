import os
from create_read_data import read_dataset

dir_db_name = 'db_DAVO'
save_path = f"{os.getcwd()}/{dir_db_name}"
file_name = 'dummy.txt'
file = os.path.join(save_path, file_name)

data = read_dataset(file)

def results(data):
  names = []
  data_dict = {}
  employees = []
  same_days = ''

  for i in range(len(data)):
    line = data[i]

    names_schedule_split = line.rsplit("=")

    name = names_schedule_split[0]
    names.append(name)

    schedule = names_schedule_split[1].split(",")

    days = [a[:2] for a in schedule]
    hours = [a[2::] for a in schedule]

    days_hours_pairs = ([list(i) for i in zip(days, hours)])

    dict_placeholder = {}
    dict_placeholder['name'] = [name]
    dict_placeholder['work_days'] = days_hours_pairs
    data_dict.update(dict_placeholder)
    employees.append(data_dict.copy())

  for i, j in [[i, j] for i in range(len(names)) for j in range(i+1, len(names))]:
    matches = [(x, y) for x in employees[i]['work_days'] for y in employees[j]['work_days'] if x == y]

    if len(matches) > 0:
      same_days += f"{employees[i]['name'][0]}-{employees[j]['name'][0]}: {len(matches)}\n"
  if len(matches) == 0:
    print('No matches found')

  return print(same_days)

results(data)