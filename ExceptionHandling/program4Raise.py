while True:
    try:
        a= int(input("enter num 1 : "))
        b=int(input("enter num 2 : "))

        if a<=0 or b<0 :
            raise Exception ("negative number not allowed! please try again ")
            c=a/b
            print("div c is ",c)
            break


    except ValueError:
        print("please inter the integer value ");
    
    except ZeroDivisionError:
        print("please enter the non-zero denominator")
    
    except Exception as e:
        print(e)

 

