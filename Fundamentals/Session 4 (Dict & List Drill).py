#Session 4 (Drill)
# 5 employees

employees = [{"Name":"KB","Hourly_rate":"200","Hours_worked":"9"},{"Name":"Aiden","Hourly_rate":"76","Hours_worked":"7"}, {"Name":"Joshua","Hourly_rate":"167","Hours_worked":"11"},{"Name":"Shawn","Hourly_rate":"110","Hours_worked":"4"}, {"Name":"Rorisang","Hourly_rate":"80","Hours_worked":"6"}]

for employee in employees:
    salary = float(employee["Hourly_rate"]) * int(employee["Hours_worked"])
    print(f"Name: {employee['Name']} Salary: R{salary}") 

tot_payroll = 0

for employee in employees:
    income = int(employee["Hourly_rate"]) * int(employee["Hours_worked"])
    tot_payroll = tot_payroll + income

print(f"Total Payroll: R{tot_payroll}")

highest_sal = 0

for employee in employees:
    salary = float(employee["Hourly_rate"]) * int(employee["Hours_worked"])
    if salary > highest_sal:
        highest_sal = salary
        highest_name = employee["Name"]

print(f"Highest Earner: {highest_name} R{highest_sal}")