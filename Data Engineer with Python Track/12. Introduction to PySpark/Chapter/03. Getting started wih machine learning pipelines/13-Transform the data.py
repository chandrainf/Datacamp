'''
Transform the data


Hooray, now you're finally ready to pass your data through the Pipeline you created!

Instructions
100 XP

- Create the DataFrame piped_data by calling the Pipeline methods .fit() and .transform() in a chain. Both of these methods take model_data as their only argument.

'''
# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)
