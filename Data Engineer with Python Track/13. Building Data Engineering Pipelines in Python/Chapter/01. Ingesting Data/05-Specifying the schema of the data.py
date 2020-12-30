'''
Specifying the schema of the data


You’re given a dataset of pricing details of diapers from several stores. After some inspection, you understand that the products have an identical schema, regardless of the store.

Since your company is already invested in Stitch, the mother company of Singer, you’ll be writing a custom Singer “tap” to export the different products in a standardized way. To do so, you will need to associate a schema with the actual data.

Example of the products for a particular shop:

    {'items': [{'brand': 'Huggies',
                'model': 'newborn',
                'price': 6.8,
                'currency': 'EUR',            
                'quantity': 40,
                'date': '2019-02-01',
                'countrycode': 'DE'            
                },
            {…}]

Instructions
100 XP

- Infer from the example above the name and the data type of each component of the store’s items. Complete the JSON schema object with this information.
- Write that schema, using the write_schema() function, to the "products" stream using the Singer API.

'''
# Complete the JSON schema
schema = {'properties': {
    'brand': {'type': 'string'},
    'model': {'type': 'string'},
    'price': {'type': 'number'},
    'currency': {'type': 'string'},
    'quantity': {'type': 'number', 'minimum': 1},
    'date': {'type': 'string', 'format': 'date'},
    'countrycode': {'type': 'string', 'pattern': "^[A-Z]{2}$"},
    'store_name': {'type': 'string'}}}

# Write the schema
singer.write_schema(stream_name='products', schema=schema, key_properties=[])
