#Single Pass Systems
#Drill 1
location_data = [{"Location":"Cape Town","Temp":17},{"Location":"Durban","Temp":12},{"Location":"Joburg","Temp":22}]

#initialize
high_temp = 0
low_temp = 100
total_temp = 0

print("----- Temperature Monitor ------")

for location in location_data:
    print(f"City: {location['Location']} Temp: {location['Temp']}\n")
    if location["Temp"] > high_temp:
        high_temp = location["Temp"]
    if location["Temp"] < low_temp:
        low_temp = location["Temp"]
    total_temp = total_temp + location["Temp"]

print(f"----------\nHighest Temp: {high_temp}\nLowest Temp: {low_temp}\nAverage Temp: {total_temp/len(location_data)}")

#Drill 2
product_data = [{"Name":"Computer","Price":1499.99,"Quantity Sold": 4},{"Name":"Keyboard","Price":499.99,"Quantity Sold": 7},{"Name":"Mouse","Price":299.99,"Quantity Sold": 10}]

#initilize
total_revenue = 0
best_revenue = 0

print("----- Store Sales Tracker ------")

for product in product_data:
    product_rev = product["Price"]*product["Quantity Sold"]
    print(f"{product['Name']} R{product_rev}")
    if product_rev > best_revenue:
        best_revenue = product_rev
        best_selling = product["Name"]
    total_revenue = total_revenue + product_rev

print(f"Total Revenue: {total_revenue}\nTop Product: {best_selling} R{best_revenue}")

#Drill 3
student_data = [{"Name":"Shawn","Test Score":76,"Assignment Score":93,"Participation Score":80},{"Name":"Bophelo","Test Score":90,"Assignment Score":63,"Participation Score":60},{"Name":"Susan","Test Score":74,"Assignment Score":88,"Participation Score":100}]

#initialize
highest_final_score = 0
class_total_score = 0
number_of_students = len(student_data)

print("----- EXAM REPORT -----")

for student in student_data:
    student_score = (student["Test Score"] + student["Assignment Score"] + student["Participation Score"])/3
    print(f"{student['Name']} Score: {student_score}")
    if student_score > highest_final_score:
        highest_final_score = student_score
        top_student = student["Name"]
    class_total_score = class_total_score + student_score

print(f"----------\nClass Average: {class_total_score/number_of_students}\nTop Student: {top_student}")