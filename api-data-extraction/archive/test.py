import shutil
# import the settings file
import config
from config import SETTINGS
# create a variable that contains the path to the staging folder
staging_folder = config.SETTINGS['staging_folder']

#write a function to create a blank csv file
def create_blank_csv_file(file_name):
    #create a blank csv file
    with open(file_name, 'w') as f:
        pass
# save the file to the staging folder
#write a function to save a csv file to the staging folder
def save_csv_file_to_staging_folder(file_name):
    #save the file to the staging folder
    shutil.copy(file_name, staging_folder)



#execute the functions
create_blank_csv_file('test.csv')
save_csv_file_to_staging_folder('test.csv')