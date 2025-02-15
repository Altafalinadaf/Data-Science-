import math
try:
    x=10/0
    print(x)
    ans=math.exp(20000)
    print(ans)
except ZeroDivisionError:
    print("Division by 0 exception occurred!")
except ArithmeticError:
    print("Numeric calculation failed!")

