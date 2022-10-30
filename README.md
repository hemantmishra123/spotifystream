#This is the Project for the json data to the tabular data conevrsion.

create an virtual environment for your project so this will create an Isolated Python Environment for The python Project. run command for creating a virtual env and isolated environment by this "python -m venv env" this will create a virtual environment name with env in windows and then activate the Virtualenv with command 
"env\scripts\activate" in windows 
First you need to setup the required package for the project to run sucessfully and run command "pip install -r requirements.txt" for installing all packages sucessfully"
after the successfully setup run command "python manage.py runserver" make sure before running serever run these Database Migartions Command is "python manage.py makemigrations" &   "python manage.py makemigrate"
After server run sucessfully upload a json file it will convert the json data first level into the tabular format and check if the File if given right or not if not raise an error for upload right json file

In the Above Code i have used file name keys.json as for the upload purposes that first saved it into the dircetory FileFolder name and then read a json file from that location and creates a pandas dataframe with keys and value coloumn .as tabular format.
