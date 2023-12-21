#advent of code day 4, number 1
import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, r"2023 Inputs/input-4-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0])

#part 1
points = 0
matches = []
count = []
for card in inputs:
    tag = card.split(': ')[0]
    all_n = card.split(': ')[1]
    winning = all_n.split(' | ')[0].split(' ')
    numbers = all_n.split(' | ')[1].split(' ')
    winning = [i for i in winning if i]
    numbers = [i for i in numbers if i]
    match = 0
    for x in numbers:
        if x in winning:
            match += 1
    matches.append(match)   #just for part 2
    count.append(1)         #just for part 2
    #just for part 1
    #if match != 0:
    #    points += 2 ** (match - 1)

#part 2
for x in range(len(matches)):
    match = matches[x]
    for i in range(match):
        count[x+i+1] += 1*count[x]

total = sum(count)

print(matches,count, total)
#print(points)



