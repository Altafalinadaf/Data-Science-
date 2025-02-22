a = "---Khadar Basha----"

# print all the numbers as lower case
print(a.lower())

#converts all the numbers as upper case
print(a.upper())


#captial leters become small and small letters become capital here
print(a.swapcase())


# Starting letther of the string will become capital remianing all are small
print(a.capitalize())

# it will remove the spaces and tabs but we need to speacify waht we need to remove
print(a.strip('-'))

# it will remove the spaces from the left side 
print(a.lstrip('-'))

# it will remove the spaces from the right side 
print(a.rstrip('-'))

b= '2'
# check wherether the b variable contains digit
print(b.isdigit())


# give the index number of particular character. if it won't find the character it will give -(minus)values
print(a.find('K'))


c = "computer"

# it will 0th index character. output = c
print(c[0])

# starting from 0 end from 2.  output = com
print(c[0:3])

# starting from 0 end from 3.  output = comp
print(c[:4])

# start from 0 end from till last
print(c[:])

# replacing the first character.. output : Computer
print(c.replace('c','C'))

print(c.replace('c','C',5))

# to check the memory location
print(id(c))