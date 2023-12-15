#advent of code day 2, number 1
import csv
import re
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, r"input-2-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0])
'''
counter = 0
for x in range(len(inputs)):
    subkey = inputs[x].split(': ')
    games = subkey[1].split('; ')
    game_id = subkey[0].split(' ')
    red_max = 12
    green_max = 13
    blue_max = 14
    all_g = 1
    for game in games:
        if "red" in game:
            sub_r = game.split(' red')
            sub_r1 = sub_r[0].split(', ')
            #print(sub_r1[0])
            if int(sub_r1[-1]) > red_max:
                all_g = 0
        if "green" in game:
            sub_g = game.split(' green')
            sub_g1 = sub_g[0].split(', ')
            if int(sub_g1[-1]) > green_max:
                all_g = 0
        if "blue" in game:
            sub_b = game.split(' blue')
            sub_b1 = sub_b[0].split(', ')
            if int(sub_b1[-1]) > blue_max:
                all_g = 0
    if all_g == 1:
        print(int(game_id[-1]), "counts")
        counter += int(game_id[-1])

print(counter)
'''

#day 2 problem 2
counter = 0
for x in range(len(inputs)):
    subkey = inputs[x].split(': ')
    games = subkey[1].split('; ')
    game_id = subkey[0].split(' ')
    red_max = 0
    green_max = 0
    blue_max = 0
    for game in games:
        if "red" in game:
            sub_r = game.split(' red')
            sub_r1 = sub_r[0].split(', ')
            #print(sub_r1[0])
            if int(sub_r1[-1]) > red_max:
                red_max = int(sub_r1[-1])
        if "green" in game:
            sub_g = game.split(' green')
            sub_g1 = sub_g[0].split(', ')
            if int(sub_g1[-1]) > green_max:
                green_max = int(sub_g1[-1])
        if "blue" in game:
            sub_b = game.split(' blue')
            sub_b1 = sub_b[0].split(', ')
            if int(sub_b1[-1]) > blue_max:
                blue_max = int(sub_b1[-1])
    
    counter += red_max * green_max * blue_max

print(counter)