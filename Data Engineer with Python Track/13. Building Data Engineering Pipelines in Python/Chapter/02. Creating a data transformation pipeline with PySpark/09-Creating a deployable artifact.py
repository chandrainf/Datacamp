'''
Creating a deployable artifact


In the video, you saw how to run a PySpark program locally by first zipping your code. This packaging step becomes more important when your code consists of many modules. Packaging in the zip format is done by navigating to the root folder of your pipeline using the cd command and running the following command:

zip --recurse-paths zip_file.zip pipeline_folder
In this exercise you will first create a zipped archive, to pass along as dependencies of your Spark job. Then you have one of the prerequisites to running a Spark job locally, which you know now is a good way to get simple issues resolved quickly.

Instructions
100XP

- In the shell, navigate to /home/repl/workspace/spark_pipelines/.
- There, create the pydiaper.zip archive using the bash command zip and its options. The compressed archive should contain all the files in the pydiaper folder (including that folder, because that’s the package imported by various modules), and those in all of the directories below.

'''
# You need to run these commands in the terminal:

cd spark_pipelines
zip - -recurse-paths pydiaper.zip pydiaper
