'''
Best practice for default arguments


One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a panda's DataFrame. Unfortunately, they used a mutable variable as a default argument value! Please show them a better way to do this so that they don't get unexpected behavior.

  def add_column(values, df=pandas.DataFrame()):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
      values (iterable): The values of the new column
      df (DataFrame, optional): The DataFrame to update.
        If no DataFrame is passed, one is created by default.

    Returns:
      DataFrame
    """
    df['col_{}'.format(len(df.columns))] = values
    return df


Instructions
100 XP

- Change the default value of df to an immutable value to follow best practices.
- Update the code of the function so that a new DataFrame is created if the caller didn't pass one.

'''


def better_add_column(values, df=None):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.
    Args:
      values (iterable): The values of the new column
      df (DataFrame, optional): The DataFrame to update.
        If no DataFrame is passed, one is created by default.
    Returns:
      DataFrame
    """
    # Update the function to create a default DataFrame
    if df is None:
        df = pandas.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
    return df
