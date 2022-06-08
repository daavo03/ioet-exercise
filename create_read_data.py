from generate_employee_worktime import employees

# Function to create the dataset for the exercise
def create_dataset(file):
  """
  Function to create a dummy dataset to test in the exercise
  """

  f = open(file, 'w')

  f.write('\n'.join(employees))

  f.close()
  print('File created')

# Function to read the dataset
def read_dataset(file):
  f = open(file, 'r')

  data_str = f.read().replace("\n"," ")

  data = list(data_str.split(" "))

  f.close()
  print('File opened!')

  return data
    


