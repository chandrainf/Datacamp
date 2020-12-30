'''

Scheduling cronjobs with crontab


As the resident data scientist, you have been asked to automate part of a data processing pipeline. You will use one of the cronjob schedules created in a previous exercise.

You will use the built in crontab functionality of this workspace to schedule a data pipeline script, extract_data.sh to run at 30 minutes past 2am every day. Running early in the morning saves a great amount of cost by utilizing cheaper server power.

You will end up in the nano text editor where you save a file with ctrl + o (press enter) and exit with ctrl + x. Useful Nano documentation is here.

At any stage you can refresh your browser window and you will get a fresh workspace to try again if you accidentally make a mistake in the workspace.


Instructions 1/3
30 XP

- Verify there are no existing cronjobs by listing them.

# crontab -l

'''


'''
Instructions 2/3
35 XP

- Use the edit command for crontab (select nano) then schedule extract_data.sh to run with Bash at 2:30am every day.

# crontab -e
# 30 2 * * * bash extract_data.sh

'''


'''
Instructions 3/3
35 XP

-Verify the cronjob has been scheduled in the crontab by listing all current scheduled cronjobs.

# crontab -l

'''
