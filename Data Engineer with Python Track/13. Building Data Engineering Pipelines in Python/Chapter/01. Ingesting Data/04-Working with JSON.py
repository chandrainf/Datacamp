'''
Working with JSON


Because JSON is ubiquitous, you should be able to read and write this format. As you will see in the next lesson, many configuration files in Singer hold JSON.

In this exercise, you will write some configuration details of a database to a JSON file. Doing this is good practice by the way, as it keeps hardcoded parts out of your code, which allows other people to reference the same configuration files using other languages even.

Do not hesitate to refer to the slides, available in the tab on the right of IPython Shell, if you’re stuck.

Instructions
100 XP

- Import the Python module we need to deal with JSON.
- Open a file with the name database_config.json for writing (and only for writing).
- Serialize the database_address dictionary as JSON and write it to the open file handle. If you’re unsure which arguments the function takes, type ?json.dump to get more information on what obj and fp expect.

'''
# Import json
import json

database_address = {
    "host": "10.0.0.5",
    "port": 8456
}

# Open the configuration file in writable mode
with open("database_config.json", "w") as fh:
  # Serialize the object in this file handle
    json.dump(obj=database_address, fp=fh)
