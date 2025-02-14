n =int(input("enter the number "))

fact = 1

i=n
while(n>0):
    fact*=n
    n-=1
    
print("{} factorial is {}".format(i,fact))
