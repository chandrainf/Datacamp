'''
Assemble a vector


The last step in the Pipeline is to combine all of the columns containing our features into a single column. This has to be done before modeling can take place because every Spark modeling routine expects the data to be in this form. You can do this by storing each of the values from a column as an entry in a vector. Then, from the model's point of view, every observation is a vector that contains all of the information about it and a label that tells the modeler what value that observation corresponds to.

Because of this, the pyspark.ml.feature submodule contains a class called VectorAssembler. This Transformer takes all of the columns you specify and combines them into a new vector column.

Instructions
100 XP

- Create a VectorAssembler by calling VectorAssembler() with the inputCols names as a list and the outputCol name "features".
- The list of columns should be ["month", "air_time", "carrier_fact", "dest_fact", "plane_age"]

'''

# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact",
                                           "dest_fact", "plane_age"],
                                outputCol="features")
