#advent of code day 12
import time
import csv
import os
from functools import lru_cache

start_time = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

springs = []
groups = []
with open(os.path.join(__location__, "2023 Inputs/input-12-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        springs.append(row[0].split(' ')[0])
        groups.append(row[0].split(' ')[1].split(','))

groups = [tuple([int(x) for x in group]) for group in groups]

time_s = time.time() - start_time

@lru_cache
def counter(spring, group):
    #really weird one to conecptualize
    #cache the patterns so its stored in memory for faster compute time
    if spring == "":
        return 1 if group == () else 0
    
    if group == ():
        return 0 if "#" in spring else 1
    
    result = 0
    if spring[0] in ".?":
        #if first spring is . or ? that could be ., recurse to next level down
        result += counter(spring[1:],group)

    if spring[0] in "#?":
        #assume first spring is # or ? that could be #
        if group[0] <= len(spring) and "." not in spring[:group[0]] and (group[0] == len(spring) or spring[group[0]] != "#"):
            #if the grouping fits in the str of springs and there isnt a . in the str of springs and the group is the exact len of str or the next spring is not a # already
            result += counter(spring[group[0] + 1:], group[1:])

    return result

total = 0
for i, x, in enumerate(springs):
    total += counter(x, groups[i])

time_p1 = time.time() - start_time - time_s
print("The solution to Part 1 is {} which took {:.4f} seconds to run".format(total, time_p1))

@lru_cache
def expand(spring, group):
    #expands the map of springs and groupings 5x
    spring = "?".join([spring]*5)
    group *= 5

    return spring, group

total = 0 
for i, x in enumerate(springs):
    new_s, new_g = expand(x, groups[i])
    total += counter(new_s, new_g)

time_p2 = time.time() - start_time - time_p1
print("The solution to Part 2 is {} which took {:.4f} seconds to run".format(total, time_p2))
