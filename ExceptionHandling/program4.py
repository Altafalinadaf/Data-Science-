# print(10/0); # ZeroDivisionError 

try:
    print(10/0);
except ZeroDivisionError:
    print("handled")