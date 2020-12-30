'''
Pages of particle-prized people


You and a friend want to set up a website that gives information on Nobel laureates with awards relating to particle phenomena. You want to present these laureates one page at a time, with three laureates per page. You decide to order the laureates chronologically by award year. When there is a "tie" in ordering (i.e. two laureates were awarded prizes in the same year), you want to order them alphabetically by surname.

Instructions
100 XP

- Complete the function get_particle_laureates that, given page_number and page_size, retrieves a given page of prize data on laureates who have the word "particle" (use $regex) in their prize motivations ("prizes.motivation"). Sort laureates first by ascending "prizes.year" and next by ascending "surname".
- Collect and save the first nine pages of laureate data to pages.

'''
from pprint import pprint

# Write a function to retrieve a page of data


def get_particle_laureates(page_number=1, page_size=3):
    if page_number < 1 or not isinstance(page_number, int):
        raise ValueError("Pages are natural numbers (starting from 1).")
    particle_laureates = list(
        db.laureates.find(
            {'prizes.motivation': {'$regex': "particle"}},
            ["firstname", "surname", "prizes"])
        .sort([('prizes.year', 1), ('surname', 1)])
        .skip(page_size * (page_number - 1))
        .limit(page_size))
    return particle_laureates


# Collect and save the first nine pages
pages = [get_particle_laureates(page_number=page) for page in range(1, 9)]
pprint(pages[0])
