'''
Using %mprun: Hero BMI 2.0


Let's see if using a different approach to calculate the BMIs can save some memory. If you remember, each hero's height and weight is stored in a numpy array. That means you can use NumPy's handy array indexing capabilities and broadcasting to perform your calculations. A function named calc_bmi_arrays has been created and saved to a file titled bmi_arrays.py. For convenience, it is displayed below:

    def calc_bmi_arrays(sample_indices, hts, wts):

        # Gather sample heights and weights as arrays
        s_hts = hts[sample_indices]
        s_wts = wts[sample_indices]

        # Convert heights from cm to m and square with broadcasting
        s_hts_m_sqr = (s_hts / 100) ** 2

        # Calculate BMIs as an array using broadcasting
        bmis = s_wts / s_hts_m_sqr

        return bmis

Notice that this function performs all necessary calculations using arrays.

Let's see if this updated array approach decreases your memory footprint:

Load the memory_profiler package into your IPython session.
Import calc_bmi_arrays from bmi_arrays.
Once you've completed the above steps, use %mprun to profile the calc_bmi_arrays() function acting on your superheroes data. The sample_indices array, hts array, and wts array have been loaded into your session.
After you've finished coding, answer the following question:

How much memory do the array indexing and broadcasting lines of code consume in the calc_bmi_array() function? (i.e., what is the total sum of the Increment column for these four lines of code?)

Instructions
50 XP

Possible Answers

    - 10.0 MiB - 15.0 MiB

    - 0.0 MiB

    - 20.0 MiB - 30.0 MiB

    - 0.1 MiB - 2.0 MiB

Answer : 0.1 MiB - 2.0 MiB

'''
