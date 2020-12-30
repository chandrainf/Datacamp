'''
Turning columns into rows


In the previous exercise, you turned the names of the products you had in the rows into columns, and then you summarized the units of the products for every year.

Suppose you stored the result from the previous exercise in a new table called pivot_sales, and now you want to turn the columns notebooks, pencils, and crayons into row values.

The expected result will be:

    | year_of_sale | units | product_name |
    |--------------|-------|--------------|
    | 2018         | 150   | notebooks    |
    | 2018         | 150   | pencils      |
    | 2018         | 80    | crayons      |
    | 2019         | 230   | notebooks    |
    | 2019         | 130   | pencils      |
    | 2019         | 170   | crayons      |

Instructions
100 XP

- Use the appropriate operator to convert columns into rows.
- Write the name of the resulting column that will contain the turned columns.
- Write the names of the columns you want to turn into rows.
- Give to the UNPIVOT operator the alias unpivot_sales.

'''
SELECT * FROM pivot_sales
-- Use the operator to convert columns into rows
UNPIVOT
-- The resulting column that will contain the turned columns into rows
(units FOR product_name IN(notebooks, pencils, crayons))
-- Give the alias name
AS unpivot_sales
