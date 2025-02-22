import shelve

with shelve.open('my_shelf') as shelf:
    shelf['key1']={'name':'alice','age':30}
    shelf['key2'] = [1,2,3]

with shelve.open('my_shelf') as shelf:
    print(shelf['key1'])

    print(shelf['key2'])