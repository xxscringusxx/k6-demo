name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

person = {"zipcode": "12345"}

person["name"] = name
person["age"] = age 
person["city"] = city

for key, value in person.items():
    print(f"{key}: {value}")