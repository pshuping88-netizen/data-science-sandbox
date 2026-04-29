#Given Data Set
nums = [2, 5, 7, 10, 3, 8, 1]

#Double High Values

thres = 5

double_high_list = []

for n in nums:
    if n > thres:
        double_high_list.append(n*2)

print(double_high_list)

#High & Low categorizing

high_low_list = []
for n in nums:
    if n > thres:
        high_low_list.append("High")
    else:
        high_low_list.append("Low")

print(high_low_list)

#Count High & Low values

high_count = 0
low_count = 0

for n in nums:
    if n > thres:
        high_count += 1
    else:
        low_count += 1

print(high_count)
print (low_count)
