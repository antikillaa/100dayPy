def loging_decorator(function):
    def wrapper(*args, **kwargs):
        print(function(args))
        print(function(kwargs))

    return wrapper


@loging_decorator
def print_text(text):
    print(text)


print_text(text="hello")
