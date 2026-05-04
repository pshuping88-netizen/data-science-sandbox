#Function Basics
#Drill 1
def Add_function(a,b):
    c = a + b
    print(c)

def Subtract_function(a,b):
    c = b - a
    print(c)

Add_function(1,2)
Subtract_function(1,2)

#Drill 2
def functionA(a,b):
    c = a + b
    return c

def functionB(a,b):
    c = a * b
    return c

def functionC(a):
    b = a*a
    return b

#Drill 3
#turn this into a function 'salary = hourly_rate * hours_worked'
def salary_calc(a,b):
    c = a * b
    return c

#Drill 4
def high_low_func(a):
    if a > 10:
        print("Higher than you")
    else:
        print("Lower than your hopes")

high_low_func(5)
high_low_func(12)
high_low_func(20)

