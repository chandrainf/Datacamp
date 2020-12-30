'''
Doing our share of data validation


In our Nobel prizes collection, each document has an array of laureate subdocuments "laureates", each containing information such as the prize share for a laureate:

    {'_id': ObjectId('5bc56145f35b634065ba1997'),
    'category': 'chemistry',
    'laureates': [{'firstname': 'Frances H.',
    'id': '963',
    'motivation': '"for the directed evolution of enzymes"',
    'share': '2',
    'surname': 'Arnold'},
    {'firstname': 'George P.',
    'id': '964',
    'motivation': '"for the phage display of peptides and antibodies"',
    'share': '4',
    'surname': 'Smith'},
    {...

Each "laureates.share" value appears to be the reciprocal of a laureate's fractional share of that prize, encoded as a string. For example, a laureate "share" of "4" means that this laureate received a 
 
 share of the prize. Let's check that for each prize, all the shares of all the laureates add up to 1!

Notice the quotes around the values in the "share" field: these values are actually given as strings! You'll have to convert then to numbers before you find the reciprocals and add up the shares.

Instructions
100 XP

- Save a list of prizes (prizes), projecting out only the "laureates.share" values for each prize.
- For each prize, compute the total share as follows:
    - Initialize the variable total_share to 0.
    - Iterate over the laureates for each prize, converting the "share" field of the "laureate" to float and adding the reciprocal of it (that is, 1 divided by it) to total_share.

'''
# Save documents, projecting out laureates share
prizes = db.prizes.find({}, ["laureates.share"])

# Iterate over prizes
for prize in prizes:
    # Initialize total share
    total_share = 0

    # Iterate over laureates for the prize
    for laureate in prize["laureates"]:
        # add the share of the laureate to total_share
        total_share += 1 / float(laureate['share'])

    # Print the total share
    print(total_share)
