'''
Executing Python script on the command line


Let's work through an example of how we can use Python on the command line without needing to open up a GUI like Jupyter Notebook or Spyder. Interacting with Python on the command line is faster and more efficient than using a GUI. Here, we will create a Python file and execute it using our native Python, all without leaving the bash terminal.

Instructions
100 XP

- In one step, create a new Python file and pass the Python print command into the file.
- Execute the new Python file by calling it directly from the command line.

'''
# in one step, create a new file and pass the print function into the file
echo "print('This is my first Python script')" > my_first_python_script.py

# check file location
ls

# check file content
cat my_first_python_script.py

# execute Python script file directly from command line
python my_first_python_script.py
