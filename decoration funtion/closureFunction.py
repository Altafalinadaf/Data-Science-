def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


closure_function = outer_function("hello world")

closure_function()
