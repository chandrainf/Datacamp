'''
Sorting together: MongoDB + Python


In this exercise you'll explore the prizes in the physics category.You will use Python to sort laureates for one prize by last name, and then MongoDB to sort prizes by year:

  1901: Röntgen
  1902: Lorentz and Zeeman
  1903: Becquerel and Curie and Curie, née Sklodowska

You'll start by writing a function that takes a prize document as an argument, extracts all the laureates from that document, arranges them in alphabetical order, and returns a string containing the last names separated by " and ".

The Nobel database is again available to you as db. We also pre-loaded a sample document sample_doc so you can test your laureate-extracting function.

(Remember that you can always type help(function_name) in console to get a refresher on functions you might be less familiar with, e.g. help(sorted)!)

Instructions 1/3
35 XP

Complete the definition of all_laureates(prize). Within the body of the function:

    - Sort the "laureates" list of the prize document according to the "surname" key.
    - For each of the laureates in the sorted list, extract the "surname" -field.
    - The code for joining the last names into a single string is already written for you.

Take a look at the console to make sure the output looks like what you'd expect!

'''
from operator import itemgetter


def all_laureates(prize):
  # sort the laureates by surname
  sorted_laureates = sorted(prize['laureates'], key=itemgetter('surname'))

  # extract surnames
  surnames = [laureate["surname"] for laureate in sorted_laureates]

  # concatenate surnames separated with " and "
  all_names = " and ".join(surnames)

  return all_names


# test the function on a sample doc
print(all_laureates(sample_prize)



'''
Instructions 2/3
35 XP

- Find the documents for the prizes in the physics category, sort them in chronological order (by "year", ascending), and only fetch the "year", "laureates.firstname", and "laureates.surname" fields.

'''

from operator import itemgetter

def all_laureates(prize):
  # sort the laureates by surname
  sorted_laureates=sorted(prize["laureates"], key=itemgetter("surname"))

  # extract surnames
  surnames=[laureate["surname"] for laureate in sorted_laureates]

  # concatenate surnames separated with " and "
  all_names=" and ".join(surnames)

  return all_names

# find physics prizes, project year and name, and sort by year
docs=db.prizes.find(
           filter={"category": "physics"},
           projection=["year", "laureates.firstname", "laureates.surname"],
           sort=[("year", 1)])








'''
Instructions 3/3
30 XP

- Now that you have the prizes, and the function to extract laureates from a prize, print the year and the names of the laureates (use your all_laureates() function) for each prize document.

'''

from operator import itemgetter

def all_laureates(prize):
  # sort the laureates by surname
  sorted_laureates=sorted(prize["laureates"], key=itemgetter("surname"))

  # extract surnames
  surnames=[laureate["surname"] for laureate in sorted_laureates]

  # concatenate surnames separated with " and "
  all_names=" and ".join(surnames)

  return all_names

# find physics prizes, project year and name, and sort by year
docs=db.prizes.find(
           filter={"category": "physics"},
           projection=["year", "laureates.firstname", "laureates.surname"],
           sort=[("year", 1)])

# print the year and laureate names (from all_laureates)
for doc in docs:
    print("{year}: {names}".format(year=doc['year'], names=all_laureates(doc)))
