
# Create three decorators: make_bold, make_italic, make_underline, 
#   which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.
def make_bold(func):
    def wrapper(*args, **kwargs):
        retval = f'<b>{func(*args, **kwargs)}</b>'
        return retval
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        retval = f'<i>{func(*args, **kwargs)}</i>'
        return retval
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        retval = f'<u>{func(*args, **kwargs)}</u>'
        return retval
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
