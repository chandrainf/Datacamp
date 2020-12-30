'''
Create the pipeline


You're finally ready to create a Pipeline!

Pipeline is a class in the pyspark.ml module that combines all the Estimators and Transformers that you've already created. This lets you reuse the same modeling process over and over again by wrapping it up in one simple object. Neat, right?

Instructions
100 XP

- Import Pipeline from pyspark.ml.
- Call the Pipeline() constructor with the keyword argument stages to create a Pipeline called flights_pipe.
    -stages should be a list holding all the stages you want your data to go through in the pipeline. Here this is just: [dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler]


'''
# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder,
                                carr_indexer, carr_encoder,
                                vec_assembler])
