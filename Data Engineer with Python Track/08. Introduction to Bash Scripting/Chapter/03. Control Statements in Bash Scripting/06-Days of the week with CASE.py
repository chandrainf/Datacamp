'''
Days of the week with CASE


In your role as a Data Scientist, it is sometimes useful to associate dates with a 'working day' (Monday, Tuesday, Wednesday, Thursday, Friday) or a 'weekend' (Saturday & Sunday).

Your task is to build a small Bash script that will be useful to call in many areas of your data pipeline. It must take in a single argument (string of a day) into ARGV and use a CASE statement to print out whether the argument was a weekday or a weekend. You only need to account for the capitalized case for now.

You also don't need to worry about words or letters before and after. Just use exact matching for this example.

Remember the basic structure of a case statement is:

  case MATCHVAR in
    PATTERN1)
    COMMAND1;;
    PATTERN2)
    COMMAND2;;
    *)
    DEFAULT COMMAND;;
  esac

Instructions
100XP

- Build a CASE statement that matches on the first ARGV element.
- Create a match on each weekday such as Monday, Tuesday etc. using OR syntax on a single line, then a match on each weekend day (Saturday and Sunday) etc. using OR syntax on a single line.
- Create a default match that prints out Not a day! if none of the above patterns are matched.
- Save your script and run in the terminal window with Wednesday and Saturday to test.

'''
# Create a CASE statement matching the first ARGV element
case $1 in
  # Match on all weekdays
  Monday | Tuesday | Wednesday | Thursday | Friday)
  echo "It is a Weekday!"; ;
  # Match on all weekend days
  Saturday | Sunday)
  echo "It is a Weekend!"; ;
  # Create a default
  *)
  echo "Not a day!"; ;
esac



'''
# Run following in command
bash script.sh Wednesday
bash script.sh Saturday

'''
