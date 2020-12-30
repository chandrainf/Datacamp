'''
How can I view a file's contents piece by piece?


You can use cat to print large files and then scroll through the output, but it is usually more convenient to page the output. The original command for doing this was called more, but it has been superseded by a more powerful command called less. (This kind of naming is what passes for humor in the Unix world.) When you less a file, one page is displayed at a time; you can press spacebar to page down or type q to quit.

If you give less the names of several files, you can type :n (colon and a lower-case 'n') to move to the next file, :p to go back to the previous one, or :q to quit.

Note: If you view solutions to exercises that use less, you will see an extra command at the end that turns paging off so that we can test your solutions efficiently.

Instructions
100 XP

Use less seasonal/spring.csv seasonal/summer.csv to view those two files in that order. Press spacebar to page down, :n to go to the second file, and :q to quit.

Solution :

# Run the following command
| cat' part here:
less seasonal/spring.csv seasonal/summer.csv | cat

'''
