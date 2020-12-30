'''
Load JSON data


Many open data portals make available JSONs datasets that are particularly easy to parse. They can be accessed directly via URL. Each object is a record, all objects have the same set of attributes, and none of the values are nested objects that themselves need to be parsed.

The New York City Department of Homeless Services Daily Report is such a dataset, containing years' worth of homeless shelter population counts. You can view it in the console before loading it to a data frame with pandas's read_json() function.

Instructions
100 XP

- Get a sense of the contents of dhs_daily_report.json, which are printed in the console.
- Load pandas as pd.
- Use read_json() to load dhs_daily_report.json to a data frame, pop_in_shelters.
- View summary statistics about pop_in_shelters with the data frame's describe() method.

'''
# Load pandas as pd
import pandas as pd

# Load the daily report to a data frame
pop_in_shelters = pd.read_json("dhs_daily_report.json")

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())
