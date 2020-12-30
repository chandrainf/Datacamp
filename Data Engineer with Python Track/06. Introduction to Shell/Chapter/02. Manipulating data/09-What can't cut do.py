'''
What can't cut do?


cut is a simple-minded command. In particular, it doesn't understand quoted strings. If, for example, your file is:

    Name,Age
    "Johel,Ranjit",28
    "Sharma,Rupinder",26

then:

    cut -f 2 -d , everyone.csv

will produce:

    Age
    Ranjit"
    Rupinder"

rather than everyone's age, because it will think the comma between last and first names is a column separator.

What is the output of cut -d : -f 2-4 on the line:

    first:second:third:

(Note the trailing colon.)

Instructions
50 XP

Possible Answers

    - second

    - second:third

    - second:third:

    - None of the above, because there aren't four fields.

Answer : second:third:

'''
