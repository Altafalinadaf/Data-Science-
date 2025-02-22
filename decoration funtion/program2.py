def simple_decorator(fun):
    def wrapper():
        print("Something is happening before the function is called ")
        fun()
        print("something is happening after the function is called")
    return wrapper

@simple_decorator
def say_hello():
    print("hello")

say_hello()