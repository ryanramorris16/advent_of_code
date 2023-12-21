#advent of code day 10
import time
import csv
import os

start_time = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, r"2023 Inputs/input-10-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for ind, row in enumerate(reader):
        r = []
        for i2, symbol in enumerate(row[0]):
            r.append(symbol)
            if symbol == "S":
                start = [ind, i2]
        inputs.append(r)

symbols = {"|":[0,1], "-":[2,3], "L":[0,2], "J":[0,3], "7":[1,3], "F":[1,2]}
path_pos = [start]
path_dist = [0]

def follow(position, distance):
    #take a position in (row, column) and follow the pipe to the next position
    #check all neighbors except previous without distance?
    
    north = inputs[position[0] - 1][position[1]] if position[0] - 1 >= 0 else None
    south = inputs[position[0] + 1][position[1]] if position[0] + 1 < len(inputs) else None
    east = inputs[position[0]][position[1] + 1] if position[1] + 1 < len(inputs[0]) else None
    west = inputs[position[0]][position[1] - 1] if position[1] - 1 >= 0 else None 
    directions = {1:north, 0:south, 3:east, 2:west}
    dir_ind = {1:[position[0] - 1,position[1]],0:[position[0] + 1,position[1]],3:[position[0],position[1] + 1],2:[position[0],position[1] - 1]}

    n_pos = []
    if distance == 0:
        #this is the starting location
        #check each of the four surrounding tiles for connections
        for nsew in directions:
            if directions.get(nsew):
                #if there is a symbol at the position N S E or W of current position
                if nsew in symbols.get(directions.get(nsew)):
                    n_pos.append(dir_ind.get(nsew))

    else:
        #if this is not the starting location
        sym = inputs[position[0]][position[1]]
        locs = list(symbols.get(sym))
        for loc in locs:
            #have to flip the direction from the original loop, whoopsies
            if loc == 1 or loc == 3:
                loc -= 1
            elif loc == 0 or loc == 2:
                loc += 1
            #check the 2 tiles this pipe connects to
            if dir_ind.get(loc) not in path_pos:
                #find the one we havent been to before
                n_pos.append(dir_ind.get(loc))
 
    if n_pos:     
        for i in n_pos:
            #if there is a next position to go to
            path_pos.append(i)
            path_dist.append(distance + 1)
    
    return n_pos, distance + 1

#Part 1
for ind, val in enumerate(path_pos):
    next_pos, next_dist = follow(val,path_dist[ind])

time_p1 = time.time() - start_time


path_pos.sort(key = lambda x: x[1])
path_pos.sort(key = lambda x: x[0])


#Part 2
wall = 0
inside = 0
mapping = []
for row in range(len(inputs)):
    #iterating over every point in the map to check if inside or out
    line = []
    left_edge = ""
    for col in range(len(inputs[0])):
        if [row,col] in path_pos:
            line.append(inputs[row][col])
            if inputs[row][col] == "|":
                #straight pipe always counts as a wall
                wall += 1
            elif inputs[row][col] in "FL":
                #F and L pipes ONLY count as a wall if they are followed up by J or 7 respectively
                #otherwise its going up and down (or vice versa) and therefore doesnt affect inside/outside of the loop
                left_edge = inputs[row][col]
            elif inputs[row][col] == "J":
                if left_edge == "F":
                    wall += 1
                left_edge = ""
            elif inputs[row][col] == "7":
                if left_edge == "L":
                    wall += 1
                left_edge = ""
        else:
            if wall % 2 == 1:
                inside += 1
                line.append("+")
            else:
                line.append(" ")

    mapping.append(''.join(line))

#print(inside)
print(mapping)

time_p2 = time.time() - start_time

print("The solution to Part 1 is {} which took {} seconds to run".format(max(path_dist), time_p1))
print("The solution to Part 2 is {} which took {} seconds to run".format(inside, time_p2))
