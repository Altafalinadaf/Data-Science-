c = open("SecondFile.txt","a")
c.write("\nhello")
c.close()

d = open("SecondFile.txt","r")
print(d.read())
d.close()
