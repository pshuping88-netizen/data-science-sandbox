#Dictionaries
phone_contact = {"Name":"Jack","Number":"000 000 0000","City":"Durban"}

print(phone_contact)

#Access Fields
print(phone_contact["Name"])
print(phone_contact["Number"])
print(phone_contact["City"])

#Modifying Fields
phone_contact["City"] = "Cape Town"
print(phone_contact["City"])

#Adding Fields
phone_contact["Email"] = "jack1234@gmail.com"
print(phone_contact["Email"])

#Safe Access (Stops Crashes)
print(phone_contact.get("Address"))

#Looping with Dictionaries
for field, value in phone_contact.items():
    print(field,value)