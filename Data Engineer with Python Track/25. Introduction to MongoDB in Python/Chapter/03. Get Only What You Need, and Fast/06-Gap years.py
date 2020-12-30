'''
Gap years


The prize in economics was not added until 1969. There have also been many years for which prizes in one or more of the original categories were not awarded.

In this exercise, you will utilize sorting by multiple fields to see which categories are missing in which years.

For now, you will just print the list of all documents, but in the next chapter, you'll learn how to use MongoDB to group and aggregate data to present this information in a more convenient format.

Instructions
100 XP

- Find the original prize categories established in 1901 by looking at the distinct values of the "category" field for prizes from year 1901.
- Fetch ONLY the year and category from all the documents (without the "_id" field).
- Sort by "year" in descending order, then by "category" in ascending order.

'''
# original categories from 1901
original_categories = db.prizes.distinct('category', {'year': '1901'})
print(original_categories)

# project year and category, and sort
docs = db.prizes.find(
    filter={},
    projection={'year': 1, 'category': 1, "_id": 0},
    sort=[('year', -1), ('category', 1)]
)

# print the documents
for doc in docs:
    print(doc)
