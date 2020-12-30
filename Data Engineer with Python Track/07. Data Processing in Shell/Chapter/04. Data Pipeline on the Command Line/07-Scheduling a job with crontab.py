'''
Scheduling a job with crontab


In this exercise, we will create a simple Python job and automate this job using CRONTAB so that it runs every minute.

If you're unsure of how to use cron or crontab, refer to https://crontab.guru for more documentation.

Instructions 1/4
25 XP

-Verify that there are currently no CRON jobs currently scheduled via CRONTAB.

'''


'''
Instructions 2/4
25 XP

-Create a Python file called hello_world.py which prints "hello world" when executed.

'''
# Verify that there are no CRON jobs currently scheduled
crontab - l

# Create Python file hello_world.py
echo "print('hello world')" > hello_world.py

# Preview Python file
cat hello_world.py


'''
Instructions 3/4
25 XP

-Modify CRONTAB by adding a job that runs the Python script hello_world.py every minute on the minute.

'''
# Verify that there are no CRON jobs currently scheduled
crontab - l

# Create Python file hello_world.py
echo "print('hello world')" > hello_world.py

# Preview Python file
cat hello_world.py

# Add as job that runs every minute on the minute to crontab
echo "* * * * * python hello_world.py" | crontab


'''
Instructions 4/4
25 XP

-Verify that the CRON job has been created successfully.

'''
# Verify that there are no CRON jobs currently scheduled
crontab - l

# Create Python file hello_world.py
echo "print('hello world')" > hello_world.py

# Preview Python file
cat hello_world.py

# Add as job that runs every minute on the minute to crontab
echo "* * * * * python hello_world.py" | crontab

# Verify that the CRON job has been added
crontab - l
