'''
Practice with NumPy arrays


Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to a numpy array's ability to vectorize operations, so they are performed on all elements of an object at once.

A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience. numpy has been imported into your session as np.

Instructions 1/2
50 XP

- Print the second row of nums.
- Print the items of nums that are greater than six.
- Create nums_dbl that doubles each number in nums.
- Replace the third column in nums with a new column that adds 1 to each item in the original column.

'''
print(nums[1, :])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums)


'''
Instructions 2/2
50 XP

Question

When compared to a list object, what are two advantages of using a numpy array?

Possible Answers

    - A numpy array is the only data structure that can be used with the numpy package and often has less verbose indexing syntax.

    - A numpy array contains homogeneous data types (which reduces memory consumption) and provides the ability to apply operations on all elements through broadcasting.

    - A numpy array supports boolean indexing and has much better one-dimensional indexing capabilities.

    - Both a list object and a numpy array are identical.

Answer : A numpy array contains homogeneous data types (which reduces memory consumption) and provides the ability to apply operations on all elements through broadcasting.

'''
