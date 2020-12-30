'''
HTML Generator


You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators that will add bold or italics tags to any function that returns a string. You notice, however, that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators, you want to create one decorator, html(), that can take any pair of opening and closing tags.

  def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '<b>{}</b>'.format(msg)
    return wrapper

  def italics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '<i>{}</i>'.format(msg)
    return wrapper

Instructions 1/4
25 XP

Return the decorator and the decorated function from the correct places in the new html() decorator.

'''


def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)
        # Return the decorated function
        return wrapper
    # Return the decorator
    return decorator


'''
Instructions 2/4
25 XP

Use the html() decorator to wrap the return value of hello() in <b> and </b> (the HTML tags that mean "bold").

'''
# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
    return 'Hello {}!'.format(name)


print(hello('Alice'))


'''
Instructions 3/4
25 XP

Use html() to wrap the return value of goodbye() in <i> and </i> (the HTML tags that mean "italics").

'''
# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
    return 'Goodbye {}.'.format(name)


print(goodbye('Alice'))


'''
Instructions 4/4
25 XP

Use html() to wrap hello_goodbye() in a DIV, which is done by adding <div> and </div> tags around a string.

'''
# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


print(hello_goodbye('Alice'))
