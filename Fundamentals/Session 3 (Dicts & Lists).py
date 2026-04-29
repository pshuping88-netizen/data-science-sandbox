#Dictionaries and Lists

#List Below (4 activities)
num_list = [12,7,4,22,13]

for n in num_list:
    print(n)


for n in num_list:
    print(n*2)

for n in num_list:
    if n > 10:
        print(n)

sum1 = 0

for n in num_list:
    sum1 = sum1 + n

print(sum1)

#Dictionary Below (3 activities)

student = {"Name":"Jody","Age":"16","Course":"Mathematics"}

print(student["Name"])
print(student["Age"])
print(student["Course"])

student["Name"] = "Reese"

student["Student Number"] = "123456789"

print(student)

for key,value in student.items():
    print(key,value)

#Combined List & Dictionaries
people = []

for i in range(3):
    person = {"Name":input("Enter Name"),"Age":input("Enter Age"),"Skill":input("Enter skill")}
    people.append(person)

for n in people:
    print(n)

for n in people:
    print(n["Name"])



#Prac Activity
list1 = []

for i in range(3):
    item = {"Name":input("Enter item name:")}
    list1.append(item)

print(list1)

num_list = [12,7,4,22,13]

for n in num_list:
    print(n)

#Dictionaries and Lists

#List Below (4 activities)
num_list = [12,7,4,22,13]

for n in num_list:
    print(n)


for n in num_list:
    print(n*2)

for n in num_list:
    if n > 10:
        print(n)

sum1 = 0

for n in num_list:
    sum1 = sum1 + n

print(sum1)

#Dictionary Below (3 activities)

student = {"Name":"Jody","Age":"16","Course":"Mathematics"}

print(student["Name"])
print(student["Age"])
print(student["Course"])

student["Name"] = "Reese"

student["Student Number"] = "123456789"

print(student)

for key,value in student.items():
    print(key,value)

#Combined List & Dictionaries
people = []

for i in range(3):
    person = {"Name":input("Enter Name"),"Age":input("Enter Age"),"Skill":input("Enter skill")}
    people.append(person)

for n in people:
    print(n)

for n in people:
    print(n["Name"])



#Prac Activity
list1 = []

for i in range(3):
    item = {"Name":input("Enter item name:")}
    list1.append(item)

print(list1)

num_list = [12,7,4,22,13]

for n in num_list:
    print(n)

