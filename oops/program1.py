class Data:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.records = [] 

    def taking_input(self):
        for i in range(4):  
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            self.records.append({"name": name, "age": age}) 
    def print_data(self):
        for record in self.records:
            print(f"Name: {record['name']}, Age: {record['age']}")


class Data:
    def __init(self, name="ali", age=23):
        self.name = name
        self.age = age
        self.records = []  # List to store multiple records

    def taking_input(self):
        for i in range(4):  # Loop from 0 to 3 (4 inputs)
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            self.records.append({"name": name, "age": age})  # Store as a dictionary

    def print_data(self):
        for record in self.records:
            print(f"Name: {record['name']}, Age: {record['age']}")

# Example Usage:
obj = Data()
obj.taking_input()
obj.print_data()
