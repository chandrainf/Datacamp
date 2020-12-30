'''
Chain taps and targets


Welcome to your first IDE exercise! This interface is similar to the one you will encounter outside of DataCamp. On the left of the righthand pane, you have a directory of folders and files. You can open the files and see the code in the right part of the pane. For now, you need to use only one file, data_lake.conf, which is already open for you, and run a command in the shell (the bottom panel). Feel free to explore the directories, though it’s not required for this exercise.Parts of an integrated development environment

Your company’s data lake, which is file system based, is made available to you under /home/repl/workspace/mnt/data_lake. Your goal is to add a file to it, using the Singer tap we’ve been building over the last few exercises, tap-marketing-api, and an already existing Singer target, target-csv.

Your Singer tap has been packaged as tap-marketing-api (you can call it like that from the bash shell, which is in the bottom panel). Its output is simply the schema and records you made earlier. You can therefore use it in a shell pipeline, like so: tap-marketing-api | some-target. Remember, some taps and targets can be configured through configuration and state files in which case you should use those flags and pass in relevant files, e.g. some-tap | target-csv --config some_config_file.

Instructions
100XP

Create a Singer pipeline that will create a file in the landing area of the data lake, holding the output of tap-marketing-api in CSV format. To do so:

- In the shell, pipe the output of your Singer “tap”, tap-marketing-api, to target-csv.
- Pass the configuration file data_lake.conf (located in the ingest folder of the data lake) to target-csv, using the --config flag. The configuration file specifies where the CSV file should be written to and should not be changed.
Execute your command and click on “Submit Answer”, below, to see if you got it right.

'''
# You need to run the following command in the
# terminal from the ~/workspace directory.
# We'll bring you there first.
# The command here is still prefixed with a '#'.
# Run everything after the '#' sign.

# tap-marketing-api | target-csv --config ingest/data_lake.conf
