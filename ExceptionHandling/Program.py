a = 10

'''
print("start the program")
# it is not possible 
print(a/0)
print("end the code")
'''

print("start")
try:
    a/0;
except ZeroDivisionError :
    print("Denometer should be zero ");

d= a+5
print(d)