'''
Practice logging 2


The following code is executed on startup:

    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                        format='%(levelname)s - %(message)s')

In the lesson we learned that Spark operations that trigger an action must be logged with care to avoid stealth loss of compute resources. You will now practice identifying logging statements that trigger an action on a dataframe or table.

A dataframe text_df is available. This dataframe is registered as a table called table1.

Instructions
100 XP

- Several log statements are provided. All of them are initially commented out. Uncomment the five statements that do not trigger an action on text_df.

'''

# Uncomment the 5 statements that do NOT trigger text_df
logging.debug("text_df columns: %s", text_df.columns)
logging.info("table1 is cached: %s",
             spark.catalog.isCached(tableName="table1"))
#logging.warning("The first row of text_df: %s", text_df.first())
logging.error("Selected columns: %s", text_df.select("id", "word"))
logging.info("Tables: %s", spark.sql("show tables").collect())
logging.debug("First row: %s", spark.sql("SELECT * FROM table1 limit 1"))
#logging.debug("Count: %s", spark.sql("SELECT COUNT(*) AS count FROM table1").collect())
