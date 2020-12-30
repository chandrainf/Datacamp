'''
PreventOrdersUpdate in action


Let's see what the newly created trigger does when you try to update some rows in the Orders table.

Run the following script to change the order quantity to 700 for order number 425:

UPDATE Orders SET Quantity = 700 WHERE OrderID = 425;

What happens when you run the code?

Instructions
50 XP

Possible Answers

    - Nothing. There is no output in the query results pane.

    - The query results pane shows an error thrown by the new trigger.

    - The update is run successfully after the trigger runs

Answer : The query results pane shows an error thrown by the new trigger.

'''
