#Functions (Turning old code into functions)
def salary_calc(a,b):
    c = a * b
    return c

print(salary_calc(200,9))
print(salary_calc(76,7))

#Drill (structured calc) (refactored)
employees = [{"Name":"KB","Hourly_rate":"200","Hours_worked":"9"},{"Name":"Aiden","Hourly_rate":"76","Hours_worked":"7"}, {"Name":"Joshua","Hourly_rate":"167","Hours_worked":"11"},{"Name":"Shawn","Hourly_rate":"110","Hours_worked":"4"}, {"Name":"Rorisang","Hourly_rate":"80","Hours_worked":"6"}]

#intializing
highest_earn = 0
tot_pay = 0

for employee in employees:
    salary = salary_calc(int(employee["Hourly_rate"]),int(employee["Hours_worked"]))
    print(f"Name: {employee['Name']} Salary: {salary}")
    tot_pay = tot_pay + salary
    if salary > highest_earn:
        highest_earn = salary
        highest_earner = employee["Name"]

print(f"Total Payroll: {tot_pay}\n Highest Earner: {highest_earner} Salary: {highest_earn}")

#Movie Rating Report (Main Drill) (refactored)
movie_data = [{"Title":"War Machine","Rating(out of 10)":6,"Watch Count":786},{"Title":"Until Dawn","Rating(out of 10)":5,"Watch Count":685},{"Title":"People We Meet On Vacation","Rating(out of 10)":7,"Watch Count":898}]

#Functions
def engagement_calc(a,b):
    c = a * b
    return c

#initializing
highest_engagement = 0
overall_engagement = 0

#Structured Output on Calculated Data
print(f"\n----- MOVIE REPORT -----")

for movie in movie_data:
    total_engagement = engagement_calc(movie["Rating(out of 10)"],movie["Watch Count"])
    overall_engagement = overall_engagement + total_engagement
    if total_engagement > highest_engagement:
        highest_engagement = total_engagement
        highest_movie = movie["Title"]
    print(f"\n{movie['Title']} Score: {total_engagement}")

print(f"\n----------\nTotal Engagement: {overall_engagement}\nTop Movie: {highest_movie}")

#Drill 3 (refactored)
student_data = [{"Name":"Shawn","Test Score":76,"Assignment Score":93,"Participation Score":80},{"Name":"Bophelo","Test Score":90,"Assignment Score":63,"Participation Score":60},{"Name":"Susan","Test Score":74,"Assignment Score":88,"Participation Score":100}]

#Functions
def score_calc(a,b,c):
    d = (a+b+c)/3
    return d

def class_total_calc(a,b):
    c = a + b
    return c

def class_avg_calc(a,b):
    c = a/b
    return c

#initialize
highest_final_score = 0
class_total_score = 0
number_of_students = len(student_data)

print("----- EXAM REPORT -----")

for student in student_data:
    student_score = score_calc(student["Test Score"],student["Assignment Score"],student["Participation Score"])
    print(f"{student['Name']} Score: {student_score}")
    if student_score > highest_final_score:
        highest_final_score = student_score
        top_student = student["Name"]
    class_total_score = class_total_calc(class_total_score,student_score)

print(f"----------\nClass Average: {class_avg_calc(class_total_score,number_of_students)}\nTop Student: {top_student}")
