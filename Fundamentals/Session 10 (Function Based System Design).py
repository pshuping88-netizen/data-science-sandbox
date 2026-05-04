#Functions
#Employee System V2

#Data
employees = [{"Name":"KB","Hourly_rate":200.00,"Hours_worked":9},{"Name":"Aiden","Hourly_rate":126.00,"Hours_worked":7}, {"Name":"Joshua","Hourly_rate":167.00,"Hours_worked":11},{"Name":"Shawn","Hourly_rate":110.00,"Hours_worked":4}, {"Name":"Rorisang","Hourly_rate":80.00,"Hours_worked":6}]

#Functions
def calculate_salary(rate,hours):
    salary = rate * hours
    return salary

def find_highest_employee(employees):
    highest_sal = 0
    for employee in employees:
        employee_sal = calculate_salary(employee["Hourly_rate"],employee["Hours_worked"])
        if employee_sal > highest_sal:
            highest_sal = employee_sal
            top_earner = employee["Name"]
    return top_earner,highest_sal

def calculate_total_payroll(employees):
    total_payroll = 0
    for employee in employees:
        employee_sal = calculate_salary(employee["Hourly_rate"],employee["Hours_worked"])
        total_payroll = total_payroll + employee_sal
    return total_payroll

print(f"----- EMPLOYEE PAYROLL -----")

#Main Loop
for employee in employees: 
    employee_sal = calculate_salary(employee["Hourly_rate"],employee["Hours_worked"])
    print(f"Name: {employee['Name']} Salary: R{employee_sal}")

top_employee = find_highest_employee(employees)
total_payroll = calculate_total_payroll(employees)

print(f"Top Employee: {top_employee[0]} Salary: R{top_employee[1]}")
print(f"Total payroll: {total_payroll}")