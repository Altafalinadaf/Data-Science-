x={1,2,3,4,3}
y={4,5,6,7,8,9}


# it will add the all unique values
print(x.union(y))

# it wil give the unique value a x 
print(x.difference(y))

#it will compare both sets then return repeated values 
print(x.intersection(y))


#compare 2 sets and return the unique values and not print repeated value in x to y 
print(x.symmetric_difference(y))