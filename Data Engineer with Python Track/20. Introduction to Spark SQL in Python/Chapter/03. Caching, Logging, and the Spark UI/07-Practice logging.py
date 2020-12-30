'''
Practice logging


The following code is executed on startup:

    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                        format='%(levelname)s - %(message)s')

You will now practice these logging operations.

Instructions
100 XP

- Log columns of text_df as debug message.
- Log whether table1 is cached as info message.
- Log first row of text_df as warning message.
- Log selected columns of text_df as error message.

'''
# Log columns of text_df as debug message
logging.debug("text_df columns: %s", text_df.columns)

# Log whether table1 is cached as info message
logging.info("table1 is cached: %s",
             spark.catalog.isCached(tableName="table1"))

# Log first row of text_df as warning message
logging.warning("The first row of text_df:\n %s", text_df.first())

# Log selected columns of text_df as error message
logging.error("Selected columns: %s", text_df.select("id", "word"))
