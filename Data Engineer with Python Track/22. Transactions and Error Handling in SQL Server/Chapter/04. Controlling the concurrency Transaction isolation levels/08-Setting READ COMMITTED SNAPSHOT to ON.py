'''
Setting READ COMMITTED SNAPSHOT to ON


The default isolation level of your database is READ COMMITTED. You made some scripts that were supposed to be run under the READ COMMITTED isolation level.

Now, you want every script you already made to be run with the READ COMMITTED SNAPSHOT option set to ON. In doing this, each statement under the READ COMMITTED isolation level will see the committed changes that occur before the start of each statement.

Which options do you need to set in your database?

Answer the question
50XP

Possible Answers

    - ALTER DATABASE myDatabaseName SET ALLOW_SNAPSHOT_ISOLATION ON and ALTER DATABASE myDatabaseName SET READ_COMMITTED_SNAPSHOT ON.

    - ALTER DATABASE myDatabaseName SET ALLOW_SNAPSHOT_ISOLATION OFF and ALTER DATABASE myDatabaseName SET READ_COMMITTED_SNAPSHOT ON.

    - ALTER DATABASE myDatabaseName SET TRANSACTION ISOLATION LEVEL SNAPSHOT and ALTER DATABASE myDatabaseName SET READ_COMMITTED_SNAPSHOT ON.

    - ALTER DATABASE myDatabaseName SET ALLOW_SNAPSHOT_ISOLATION ON, ALTER DATABASE myDatabaseName SET TRANSACTION ISOLATION LEVEL SNAPSHOT,and ALTER DATABASE myDatabaseName SET READ_COMMITTED_SNAPSHOT ON.

Answer : ALTER DATABASE myDatabaseName SET ALLOW_SNAPSHOT_ISOLATION ON and ALTER DATABASE myDatabaseName SET READ_COMMITTED_SNAPSHOT ON.

'''