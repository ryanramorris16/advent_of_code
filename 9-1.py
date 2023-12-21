#advent of code day 9
import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


history = []

with open(os.path.join(__location__, r"2023 Inputs/input-9-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        history.append((row[0].split(' ')))

for ind, row in enumerate(history):                       
    history[ind] = [int(i) for i in row]
        
def next_num(history):
    #find the next number based on a history of numbers
    #history is an array of numbers
    diff = history
    lasts = []
    firsts = []
    while any(diff):
        new = []
        for ind, num in enumerate(diff[0:-1]):
            new.append(diff[ind + 1] - num)
        lasts.append(diff[-1])
        firsts.append(diff[0])
        diff = new

    f_sum = 0
    for ind, x in enumerate(firsts):
        f_sum += ((-1) ** ind) * x

    return sum(lasts), f_sum

#Part 1 & 2

total = 0
total2 = 0
for i in history:
    total += next_num(i)[0]
    total2 += next_num(i)[1]

print(total, total2)
