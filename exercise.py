import os
from create_read_data import read_dataset

dir_db_name = 'db_DAVO'
save_path = f"{os.getcwd()}/{dir_db_name}"
file_name = 'dummy.txt'
file = os.path.join(save_path, file_name)

data = read_dataset(file)

def generate_dataset(data):
  names = []
  data_dict = {}
  employees = []

  for i in range(len(data)):
    line = data[i]

    names_schedule_split = line.rsplit("=")

    name = names_schedule_split[0]
    names.append(name)

    schedule = names_schedule_split[1].split(",")

    aa = [a[:2] for a in schedule]
    bb = [a[2::] for a in schedule]

    asd = ([list(i) for i in zip(aa, bb)])

    d0 = {}
    d0['name'] = [name]
    d0['work_days'] = asd
    data_dict.update(d0)
    employees.append(data_dict.copy())

  return (employees, names)

(dataset, names) = generate_dataset(data)


def results(dataset, names):
  same_days = ''
  for i, j in [[i, j] for i in range(len(names)) for j in range(i+1, len(names))]:
    matches = [(x, y) for x in dataset[i]['work_days'] for y in dataset[j]['work_days'] if x == y]
    if len(matches) >= 1:
      same_days += f"{dataset[i]['name'][0]}-{dataset[j]['name'][0]}: {len(matches)}\n"
  
  return print(same_days)

results(dataset, names)