#data set (list)

nums = [3,7,1,9,4,6]

#double the list

double_nums = []

for n in nums:
    double_nums.append(n*2)

print(double_nums)

#Greater than 5 list

greater_nums = []

for n in nums:
    if n > 5:
        greater_nums.append(n)

print(greater_nums)

#combined Methods list

combined_list = []

for n in nums:
    if n>5:
        combined_list.append(n*2)

print(combined_list)

#high & low list

high_low_list = []

for n in nums:
    if n>5:
        high_low_list.append("High")
    else:
        high_low_list.append("Low")

print(high_low_list)