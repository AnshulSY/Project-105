import statistics
import csv
import math
with open('/Users/anshul/Desktop/Class 105/data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
def mean(data):
    m = len(data)
    total = 0
    for x in data:
        total = total + int(x) 
    
    mean = total/m
    return mean

variance = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    variance.append(a)

sum = 0 
for i in variance:
    sum = sum + i

result = sum/len(data) 
std_ded = math.sqrt(result)
print(std_ded)
