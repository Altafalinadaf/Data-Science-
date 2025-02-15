while(True):
    try:
        a = int(input("Enter first no.:"))
        b = int(input("Enter second no.:"))
        c = a/b
        print("Division is:",c)
    
    # without exception clause name also we can write the issue is we will not know what kindda exception is 
    except:
        print("Some problem occurred.. Try again")	

