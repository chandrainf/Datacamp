'''
Streaming records


In an earlier exercise, you codified the schema of products being sold by a store that you got from the marketing team’s REST API. If you don’t remember it, check the schema in this exercise. Now it’s time to stream some data to go with it.

A convenience function, retrieve_products(), has been made available to you. It basically executes the last step of the previous exercise: it requires one positional argument, the name of a shop, and will return a list of all products related to that shop.

This exercise is pushing you to use unpacking, using the ** operator, as shown in the video. If it’s the first time you encounter the unpacking operator, fear not: there’s a first time for everything. We want to show it to you because you will encounter it in your colleagues’ scripts. Do not hesitate to refer to the slides on the tab to the right of the IPython Shell. Unpacking lets you update a record in one step, but you don’t have to use it. You can add the key-value pair outside of the function call as well, by adding a few lines of code. Use any method you like, as long as the record is defined correctly.

Instructions 1/3
35 XP

- Retrieve the products of the shop called Tesco.

'''
# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

'''
Instructions 2/3
35 XP

Based on the output of the previous step, use the function write_record() to write one of these products to the products stream, which is where you also wrote the schema to. Make sure to add to the product a key-value pair that is mentioned in the schema, but is missing from the product, so that the record you write complies with the schema.

'''
# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.write_record(stream_name="products",
                    record={**tesco_items[0], "store_name": "Tesco"})

'''
Instructions 3/3
30 XP

Now use the more appropriate function write_records() to write all items for all shops exposed by the API. As you don’t know a priori how big the dataset will be, you will be using a generator expression in which you enrich the items with the store_name one at a time.

'''
# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.write_record(stream_name="products",
                    record={**tesco_items[0], "store_name": "Tesco"})

for shop in requests.get(SHOPS_URL).json()["shops"]:
    # Write all of the records that you retrieve from the API
    singer.write_records(
        stream_name="products",  # Use the same stream name that you used in the schema
        records=({**tesco_items[0], "store_name": 'Tesco'}
                 for item in retrieve_products(shop))
    )
