'''
Model production on the command line


Often times, Python models, once perfected, need to be moved into production and run on a frequent basis. To save the data scientist's time, instead of running the model manually every day, the run process is automated.

Automating and putting a Python model into production involves first installing all necessary library dependencies, running the Python model itself, and then setting a schedule for frequency of the runs. While it is possible to do all these steps separately using different languages and programs, consolidating all efforts into command line commands allows for more user control and easier automation.

In this capstone exercise, we will practice how to set up an end-to-end Python script automation process step by step.

Instructions
100 XP

- Use pip to install the Python dependencies listed in the requirements.txt file.

- Now that the necessary Python dependencies have been installed, run the create_model.py script on the command line.

- We have verified that the Python model can be run. Next step is to automate this job so it runs every minute. Use CRONTAB to schedule a per minute run of the Python script create_model.py.

- Print the job scheduled in CRONTAB to verify that the CRON job is scheduled correctly.

'''
# Preview both Python script and requirements text file
cat create_model.py
cat requirements.txt

# Pip install Python dependencies in requirements file
pip install - r requirements.txt

# Run Python script on command line
python create_model.py

# Add CRON job that runs create_model.py every minute
echo "* * * * * python create_model.py" | crontab

# Verify that the CRON job has been scheduled via CRONTAB
crontab - l
