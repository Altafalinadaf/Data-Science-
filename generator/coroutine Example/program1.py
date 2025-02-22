def simple_coroutine():
    print("Coroutine started ")
    while True :
        x = yield
        print(f"Recieved : {x}")
   


coro = simple_coroutine()

next(coro)
coro.send(42)
coro.send(2000)
coro.send("ali")

print(type(coro))