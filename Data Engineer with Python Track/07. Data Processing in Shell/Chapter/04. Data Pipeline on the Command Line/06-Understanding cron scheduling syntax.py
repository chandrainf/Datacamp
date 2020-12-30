'''
Understanding cron scheduling syntax


Which of the following is the correct Crontab syntax for execute the Python model script (model.py) every hour, on the 15 minute of an hour? (e.g. 12:15 PM, 1:15 AM, 2:15 AM, etc)?

Remember the syntax for Crontab:

    .---------------- minute (0 - 59)
    |  .------------- hour (0 - 23)
    |  |  .---------- day of month (1 - 31)
    |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed ...
    |  |  |  |  |
    *  *  *  *  * command-to-be-executed


Instructions
50 XP

Possible Answers

    - * * * * * python model.py

    - 15 * * * * python model.py

    - 15 * * * python model.py

    - 15 * * * * model.py

Answer : 15 * * * * python model.py

'''
