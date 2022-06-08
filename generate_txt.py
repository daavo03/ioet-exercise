import os
from create_read_data import create_dataset

dir_db_name = 'db_DAVO'
save_path = f"{os.getcwd()}/{dir_db_name}"
file_name = 'data.txt'
new_file = os.path.join(save_path, file_name)

# Check if the dir/file exists
dir_exist = os.path.exists(save_path)
file_exist = os.path.exists(new_file)

# Creating the dir/file for our dataset
if dir_exist and file_exist:
  print('Dataset already exists.\nGo to the new folder in this directory to get your file.')
  new_dataset = input('Do you want to create a new dataset? ')
  if new_dataset == 'yes':
    create_dataset(new_file)
  elif new_dataset == 'no':
    print('Go to the new folder in this directory to get your file.')
elif not dir_exist:
  os.mkdir(dir_db_name) 
  print('Directory for dataset created')
  create_dataset(new_file)
else:
  create_dataset(new_file)
