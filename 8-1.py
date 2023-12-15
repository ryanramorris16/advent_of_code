#advent of code day 8
import csv
import math
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

direction = []
location = []
left_dest = []
right_dest = []

with open(os.path.join(__location__, r"input-8-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for ind, row in enumerate(reader):
        if ind == 0:
            direction.append(row[0])
        elif ind > 1:
            #print(row[0].split(' '))
            location.append(row[0].split(' ')[0])
            left_dest.append(row[0].split(' ')[2][1:-1])
            right_dest.append(row[0].split(' ')[3][0:-1])

dir_num = []
for i in direction[0]:
    #print(i)
    if i == "L":
        dir_num.append(0)
    elif i == "R":
        dir_num.append(1)

def l_or_r(loc, direc):
    #takes location and a direction to point to next destination
    index = location.index(loc)
    if direc == 0:
        dest = left_dest[index]
    elif direc == 1:
        dest = right_dest[index]

    return dest

#Part 1
#a follow the directions until dest is ZZZ
'''
loc = "AAA"
step = 0
total = 0
while loc != "ZZZ":
    print(loc)
    loc = l_or_r(loc,dir_num[step])
    if step < len(dir_num) - 1:
        step += 1
        total += 1
    elif step == len(dir_num) - 1:
        step = 0
        total += 1
'''

#Part 2
#follow every node that ends in A until they all end in Z
locs = []
for loc in location:
    if loc[-1] == "A":
        locs.append(loc)

tots = []
for loc in locs:
    step = 0
    total = 0
    while loc[-1] != "Z":
        loc = l_or_r(loc, dir_num[step])
        if step < len(dir_num) - 1:
            step += 1
            total += 1
        elif step == len(dir_num) - 1:
            step = 0
            total += 1
    tots.append(total)

#print(tots)

p2_total = math.lcm(*tots)

print(p2_total)
