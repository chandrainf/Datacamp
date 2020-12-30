'''
Counter


You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.

Instructions
100 XP

- Call the function being decorated and return the result.
- Return the new decorated function.
- Decorate foo() with the counter() decorator.

'''


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)

    wrapper.count = 0
    # Return the new decorated function
    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')


foo()
foo()

print('foo() was called {} times.'.format(foo.count))
