def func1(param):
    print(param)


holder = func1
holder("hello")


def new_decorator(func):

    def wrap_func():
        print("Code before parameter func")
        func()
        print("Code after parameter func")
    return wrap_func


def func_needs_decorator():
    print("I want to be decorated!!")


decorated_func = new_decorator(func_needs_decorator)
decorated_func()

print("\n")


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator()