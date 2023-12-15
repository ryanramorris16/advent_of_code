#advent of code day 6, number 1
import csv
import math
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, r"input-6-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0])

times = [int(splits) for splits in inputs[0].split(":")[1].split(" ") if splits]
dist = [int(splits) for splits in inputs[1].split(":")[1].split(" ") if splits]

def hold(max_time, max_dist):
    
    #figure out what values of holding down the button produce results further than max_dist
    lower = list(range(1,max_time//2))
    higher = list(reversed(range(max_time//2, max_time)))
    ranges = []
    #look for first value > 0 that satisfies this condition
    for l in lower:
        speed = l
        dist = l * (max_time - l)
        if dist > max_dist:
            ranges.append(l)
            break
    #look for first value < max_time that satisfies this condition
    for h in higher:
        speed = h
        dist = h * (max_time - h)
        if dist > max_dist:
            ranges.append(h)
            break
    
    return ranges

#part 1 only
'''
ways = []
for ind, x in enumerate(times):
    ans = hold(x, dist[ind])
    print(ans)
    ways.append((ans[1]-ans[0])+1)

start = 1
for x in ways:
    start = start * x

print(start)
'''

#part 2
ftime = 0
fdist = 0
for ind, x in enumerate(times):
    #print(ftime,fdist)
    length_t = len(str(x))
    ftime = ftime * (10 ** length_t) + x
    length_d = len(str(dist[ind]))
    fdist = fdist * (10 ** length_d) + dist[ind]

#sorta brute force
'''
ranges = hold(ftime,fdist)
print(ranges[1]-ranges[0]+1)
'''
def hold_quadratic(max_time, max_dist):

    #find the zero values of the quadratic to find optimal times
    #speed = charge up time
    #distance = speed * time = charge time * (max_time - charge time)
    #distance = c_t*m_t - c_t**2
    #0 = c_t**2 - c_t*m_t + dist
    # ax**2 + bx + c = 0
    # x = -b +- sqrt(b**2-4ac)    /    2a

    a = 1
    b = -max_time
    c = max_dist

    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    print(x1, x2)
    x1 = math.ceil(x1-1)
    x2 = math.floor(x2+1)

    rng = x1-x2 + 1
    return rng

#a little cleaner using quad form
print(hold_quadratic(ftime,fdist))
total = 1
for ind,x in enumerate(times):
    ans = hold_quadratic(x, dist[ind])
    total = total * ans

print(total)



