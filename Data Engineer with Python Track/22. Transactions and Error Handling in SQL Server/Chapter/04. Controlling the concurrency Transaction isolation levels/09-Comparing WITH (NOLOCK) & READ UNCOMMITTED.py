'''
Comparing WITH (NOLOCK) & READ UNCOMMITTED


Your colleague needs to read some uncommitted data within a transaction. He has to decide whether to use WITH (NOLOCK) option or the READ UNCOMMITTED isolation level, but he is not sure about the differences between both options.

Can you help him to clarify the differences between using WITH (NOLOCK) option and the READ UNCOMMITTED isolation level?

Answer the question
50XP

Possible Answers

    - The WITH (NOLOCK) option behaves like the READ UNCOMMITTED isolation level. But, whereas the isolation level applies to a specific table, the WITH (NOLOCK) option applies for the entire connection.

    - The WITH (NOLOCK) option doesn't behave like the READ UNCOMMITTED isolation level because the first one can't read dirty reads.

    - The WITH (NOLOCK) option behaves like the READ UNCOMMITTED isolation level. But whereas the isolation level applies for the entire connection, WITH NOLOCK applies to a specific table.

    - The WITH (NOLOCK) option behaves like the READ UNCOMMITTED isolation level, because the first one can't read dirty reads.

Answer : The WITH (NOLOCK) option behaves like the READ UNCOMMITTED isolation level. But whereas the isolation level applies for the entire connection, WITH NOLOCK applies to a specific table.

'''