'''
What other wildcards can I use?


The shell has other wildcards as well, though they are less commonly used:

    -? matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
    -[...] matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
    -{...} matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.

Which expression would match singh.pdf and johel.txt but not sandhu.pdf or sandhu.txt?

Answer the question
50XP

Possible Answers

    -[sj]*.{.pdf, .txt}

    -{s*.pdf, j*.txt}

    -[singh,johel]{*.pdf, *.txt}

    -{singh.pdf, j*.txt}

Answer : {singh.pdf, j*.txt}

'''
