'''
Modifying variables outside local scope


Sometimes your functions will need to modify a variable that is outside of the local scope of that function. While it's generally not best practice to do so, it's still good to know-how in case you need to do it. Update these functions so they can modify variables that would usually be outside of their scope.

Instructions 1/3
35 XP

Add a keyword that lets us update call_count from inside the function.

'''
call_count = 0


def my_function():
    # Use a keyword that lets us update call_count
    global call_count
    call_count += 1

    print("You've called my_function() {} times!".format(
        call_count
    ))


for _ in range(20):
    my_function(







'''
Instructions 2/3
35 XP

Add a keyword that lets us modify file_contents from inside save_contents().

'''
def read_files():
    file_contents=None

    def save_contents(filename):
        # Add a keyword that lets us modify file_contents
        nonlocal file_contents
        if file_contents is None:
            file_contents=[]
        with open(filename) as fin:
            file_contents.append(fin.read())

    for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
        save_contents(filename)

    return file_contents







'''
Instructions 3/3
30 XP

Add a keyword to done in check_is_done() so that wait_until_done() eventually stops looping.

'''
def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done()
        # doesn't run forever
        global done
        if random.random() < 0.1:
            done=True

    while not done:
        check_is_done()

done=False
wait_until_done()

print('Work done? {}'.format(done))
