import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

seeds = []
s2soil = []
soil2fert = []
fert2wat = []
wat2li = []
li2temp = []
temp2hum = []
hum2loc = []
all_map = [seeds,s2soil,soil2fert,fert2wat,wat2li,li2temp,temp2hum,hum2loc]

counter = 0
with open(os.path.join(__location__, r"2023 Inputs/input-5-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for ind, row in enumerate(reader):        
        if row:
            all_map[counter].append(row[0])
        else:
            counter += 1

seeds = seeds[0].split(' ')
seeds = [int(i) for i in seeds if i.isdigit()]
all_map[0] = seeds

print('Generating maps...')
for maps in all_map[1::]:
    for ind, row in enumerate(maps[1::]):
        #print(row)
        values = row.split(' ')
        values = [int(i) for i in values if i.isdigit()]
        maps[ind+1] = values
    maps[1::] = sorted(maps[1::], key = lambda x: int(x[1]))


#for part 1
print('Generating locations from seed data...')
def seed_to_location(seed):
    orig = seed
    for maps in all_map[1::]:
        for proc in maps[1::]:
            if proc[1] <= seed < proc[1] + proc[2]:
                dif = seed - proc[1]
                seed = proc[0] + dif
                break
    location = seed
    return location, orig

locs = []
for seed in seeds:
    locs.append(seed_to_location(seed))
print(min(locs), locs)

#part 2
new_seeds = []
new_dif = []
for x in range(len(seeds)):
    if not x % 2:
        new_seeds.append(seeds[x])
        new_dif.append(seeds[x+1])

def seeds_range(start, diff):
    orig = start
    #infs = []
    src_range = [(start, start+diff-1)]
    dst_range = []
    for maps in all_map[1::]:
        for lo, hi in src_range:
            for proc in maps[1::]:

                #if the whole set is less than any of the map source values
                if hi < proc[1]:
                    dst_range.append((lo,hi))
                    break
                
                #if the start of the set is within this map line
                elif proc[1] <= lo < proc[1] + proc[2]:

                    #if the end of the set passes this map line
                    if hi >= proc[1] + proc[2]:
                        dst_range.append((proc[0] + (lo - proc[1]), proc[0] + proc[2] - 1))
                        lo = proc[1] + proc[2]
                    
                    #if the end of the set is within this map line
                    else:
                        dst_range.append((proc[0] + (lo - proc[1]), proc[0] + (hi - proc[1])))
                        break

                #end of the set is within map values, but start of the set is not
                elif lo < proc[1] and hi >= proc[1]:
                    dst_range.append((lo, proc[1] - 1))
                    lo = proc[1]
                
            #if the set is not within any map line    
            else:
                dst_range.append((lo,hi))

        src_range = dst_range
        dst_range = []

    lowest = min(lo for lo,hi in src_range)
    #print(lowest)
    return lowest

lows = []
for ind, x in enumerate(new_seeds):
    lows.append(seeds_range(x,new_dif[ind]))
    print(x, new_dif[ind], seeds_range(x,new_dif[ind]))

#print(new_seeds, new_dif)
print(min(lows))

