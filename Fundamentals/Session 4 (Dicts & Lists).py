#Lists + Loops
#rep 1
list_1 = [2,5,28,8,11]

print(list_1)

for n in list_1:
    print(n*3)

for n in list_1:
    if n > 15:
        print(n)

#rep 2
list_2 = [17,16,96,10,2]

print(list_2)

for n in list_2:
    print(n*3)

for n in list_2:
    if n > 15:
        print(n)

#rep 3
list_3 = [17,12,10,88,9]

print(list_3)

for n in list_3:
    print(n*3)

for n in list_3:
    if n > 15:
        print(n)

#Dictonaries
#rep 1
person_1 = {"Name":"Ethan","Age":"19","City":"Durban"}
print(person_1)

person_1["Name"] = "Rorisang"

person_1["Skill"] = "Writing"

print(person_1)

for key, value in person_1.items():
    print(key,value)

#rep 2
person_2 = {"Name":"Peter","Age":"22","City":"Joburg"}
print(person_2)

person_2["Age"] = "18"

person_2["School"] = "Bergvliet"

print(person_2)

for key, value in person_2.items():
    print(key,value)

#rep 3
person_3 = {"Name":"Erica","Age":"12","City":"Cape Town"}

print(person_3)

person_3["City"] = "Bloemfontein"

person_3["Fav Book"] = "GlasGow Boys"

print(person_3)

for key, value in person_3.items():
    print(key,value)

#Combined
#rep 1
listt_1 = [{"Name":"Ethan","Age":"19","City":"Durban"},{"Name":"Peter","Age":"22","City":"Joburg"},{"Name":"Erica","Age":"12","City":"Cape Town"}]

for n in listt_1:
    print(n["Name"])

#rep 2
listt_2 = [person_1,person_2,person_3]
for n in listt_2:
    print(n["Name"])
