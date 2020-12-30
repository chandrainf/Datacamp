'''
Work with JSON orientations


JSON isn't a tabular format, so pandas makes assumptions about its orientation when loading data. Most JSON data you encounter will be in orientations that pandas can automatically transform into a data frame.

Sometimes, like in this modified version of the Department of Homeless Services Daily Report, data is oriented differently. To reduce the file size, it has been split formatted. You'll see what happens when you try to load it normally versus with the orient keyword argument. The try/except block will alert you if there are errors loading the data.

pandas has been loaded as pd.

Instructions 1/2
50 XP

- Try loading dhs_report_reformatted.json without any keyword arguments.

'''

try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient="split")

    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census",
            y="total_individuals_in_shelter")
    plt.show()

except ValueError:
    print("pandas could not parse the JSON.")


'''
Instructions 2/2
50 XP

Load dhs_report_reformatted.json to a data frame with orient specified.
'''

try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient="split")

    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census",
            y="total_individuals_in_shelter")
    plt.show()

except ValueError:
    print("pandas could not parse the JSON.")
