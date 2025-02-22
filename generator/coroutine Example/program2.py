def accumulator():
    total=0
    while True:
        vl=yield total
        total+=ValueError

acc=accumulator()

next(acc)
print(acc.send(10))
print(acc.send(20))
