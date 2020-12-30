'''
Creating cronjobs


You are working as a data scientist managing an end-to-end machine learning environment in the cloud. You have created some great Bash scripts but it is becoming tedious to have to run these scripts every morning and afternoon. You recently learned about cron which you think can greatly assist here!

An example file has been placed in your directory where you can create some crontab jobs.

Remember that a crontab schedule has 5 stars relation to the time periods minute, hour, day-of-month, month-of-year, day-of-week.

Note that where all time periods are not specified in the instructions below, you can assume those time periods are 'every' (*).

Don't try to run the scripts or use crontab. Neither will work.

A useful tool for constructing crontabs is https://crontab.guru/.

Instructions
100 XP

- Create a crontab schedule that runs script1.sh at 30 minutes past 2am every day.
- Create a crontab schedule that runs script2.sh every 15, 30 and 45 minutes past the hour.
- Create a crontab schedule that runs script3.sh at 11.30pm on Sunday evening, every week. For this task, assume Sunday is the 7th day rather than 0th day (as in some unix systems).

'''
# Create a schedule for 30 minutes past 2am every day
30 2 * * * bash script1.sh

# Create a schedule for every 15, 30 and 45 minutes past the hour
15, 30, 45 * * * * bash script2.sh

# Create a schedule for 11.30pm on Sunday evening, every week
30 23 * * 7 bash script3.sh
