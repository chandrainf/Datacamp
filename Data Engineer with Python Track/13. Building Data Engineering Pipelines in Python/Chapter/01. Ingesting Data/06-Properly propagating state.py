'''
Properly propagating state


You’re running a Singer tap daily at midnight, to synchronize changes between databases. Your tap, called tap-mydelta, extracts only the records that were updated in this database since your last retrieval. To do so, your tap keeps state: it keeps track of the last record it reported on, which can be derived from the table’s last_updated_on field.

Imagine this table to reflect the current contents of the database in which updates are sometimes being made.

    id	name	last_updated_on
    1	Adrian	2019-06-14T12:00:04.000+02:00
    2	Ruanne	2019-06-16T18:33:21.000+02:00
    3	Hillary	2019-06-12T10:05:12.000+02:00

What should the state message be after you run

tap-mydelta --state last_state.json --config db_config.json
now, with the contents of last_state.json being

    {"max_last_updated_on": "2019-06-16T18:33:21.000+02:00"}

Answer the question
50XP

Possible Answers :

    - {"type": "STATE", "value": {"max-last-updated-on": "2019-06-14T12:00:04.000+02:00"}}

    - {"type": "STATE", "value": {"max-last-updated-on": "2019-06-16T18:33:21.000+02:00"}}

    - {"type": "STATE", "value": {"max-last-updated-on": "2019-06-12T10:05:12.000+02:00"}}

    - {"type": "STATE", "value": {"max-last-updated-on": "null"}}

    - No state message should be emitted.

Answer : {"type": "STATE", "value": {"max-last-updated-on": "2019-06-16T18:33:21.000+02:00"}}

'''
