'''
Turning rows into columns


In this lesson, you learned that PIVOT turns the unique values from one column into multiple columns.

Analyzing the data of paper_shop_monthly_sales, you realize the structure of this table is not appropriate for the report that you want to make.

You want to generate a report with this appearance:

	|year_of_sale|notebooks|pencils|crayons|
	|------------|---------|-------|-------|
	| 2018       | 150     | 150   | 80    |
	| 2019       | 230     | 130   | 170   |

In other words, you want to change the data you have in the rows to data into columns, and sum the units for every year.

As you learned from the previous exercises, the name of the products and the units has to be split. This is done in the subselect, take a look at it.

Instructions
100 XP

- Select the pivoted columns for every product.
- Include the sum of the units inside the PIVOT operator.
- After the FOR statement, include the name of the column that contains the values that will become column headers.
- Give to the PIVOT operator the name paper_shop_pivot.

'''
SELECT
	year_of_sale,
    -- Select the pivoted columns
	notebooks, 
	pencils, 
	crayons
FROM
   (SELECT 
		SUBSTRING(product_name_units, 1, charindex('-', product_name_units)-1) product_name, 
		CAST(SUBSTRING(product_name_units, charindex('-', product_name_units)+1, len(product_name_units)) AS INT) units,	
    	year_of_sale
	FROM paper_shop_monthly_sales) sales
-- Sum the units for column that contains the values that will be column headers
PIVOT (SUM(units) FOR product_name IN (notebooks, pencils, crayons))
-- Give the alias name
AS paper_shop_pivot

