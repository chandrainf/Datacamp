'''
Working with DATEFROMPARTS()


In this lesson, you also learned how to combine different parts of a date, which are in separate columns into one.

In the paper_shop_daily_sales table, the columns year_of_sale, month_of_sale, and day_of_sale, store the different values of a date.

    | product_name | units | year_of_sale | month_of_sale | day_of_sale |
    |--------------|-------|--------------|---------------|-------------|
    | notebooks    | 2     | 2019         | 1             | 1           |
    | notebooks    | 3     | 2019         | 5             | 12          |
    | ...          | ...   | ...          | ...           | ...         |

You need to combine all these columns into one, by using the DATEFROMPARTS() function.

Instructions 1/2
50 XP

- Use the DATEFROMPARTS() to concatenate the different parts of the date.

'''
SELECT
product_name,
units,
-- Use the function to concatenate the different parts of the date
DATEFROMPARTS(
    year_of_sale,
    month_of_sale,
    day_of_sale) AS complete_date
FROM paper_shop_daily_sales

'''

Instructions 2/2
50 XP

Question :

Which of the following statements about DATEFROMPARTS() is true?

Possible Answers

    - If one argument passed to DATEFROMPARTS() has a NULL value, it will return NULL.

    - If one argument passed to DATEFROMPARTS() has a NULL value, it will return the concatenation of the rest of the arguments.

    - If one argument passed to DATEFROMPARTS() has a NULL value, it will return an error.

Answer : If one argument passed to DATEFROMPARTS() has a NULL value, it will return NULL.

'''
