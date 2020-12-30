'''
Running a Python model


In the previous exercise, we installed the packages necessary to run a Python model script. In this exercise, we'll run a pre-written Python script create_model.py which will output two things: a Python model in a saved .pkl file and the predicted scores in a saved .csv file.

Instructions 1/2
50 XP

-Use pip to list and verify that the libraries specified in create_model.py have been installed.

'''
# Re-install requirements
pip install - r requirements.txt

# Preview Python model script for import dependencies
cat create_model.py

# Verify that dependencies are installed
pip list


'''
Instructions 2/2
50 XP

-Run the Python script create_model.py from the command line.

'''
# Re-install requirements
pip install - r requirements.txt

# Preview Python model script for import dependencies
cat create_model.py

# Verify that dependencies are installed
pip list

# Execute Python model script, which outputs a pkl file
python create_model.py

# Verify that the model.pkl file has been created
ls
