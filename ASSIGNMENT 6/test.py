def func_2(func):
    def wrapper(x):
        x**=3
        return func(x)
    return wrapper

@func_2
def func_1(func):
    def wrapper(x):
        x*=2
        return func(x)
    return wrapper


@func_1
def func(x):
    return x+2

x= func(10)
print(x)
# print(func_2(func_1(func))(10))
