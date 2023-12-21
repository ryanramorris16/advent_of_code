#advent of code day 15
import time
import csv
import os

start_time = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []
with open(os.path.join(__location__, "input-15-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0].split(','))

time_s = time.time() - start_time

def hasher(stringChar):
    #stringChar - string of characters to be converted with the ascii hash
    hashValue = 0
    for letter in stringChar:
        hashValue += ord(letter)
        hashValue *= 17
        hashValue = hashValue % 256

    return hashValue

#Part 1
total = 0
for strings in inputs[0]:
    total += hasher(strings)

time_p1 = time.time() - start_time - time_s
print("The solution to Part 1 is {} which took {:.4f} seconds to run".format(total, time_p1))

def removeLens(label, boxes):
    #send label (char str) through hasher to get which box lens is removed from
    boxNum = hasher(label)
    for lens in boxes[boxNum]:
        if label in lens:
            boxes[boxNum].remove(lens)
            break

    return boxes

def addLens(label, labelNum, boxes):
    #send label (char str) through hasher to get which box lens is added to
    boxNum = hasher(label)
    if boxes[boxNum]:
        for ind, lens in enumerate(boxes[boxNum]):
            if label in lens:
                boxes[boxNum][ind] = '{} {}'.format(label, labelNum)
                break
            elif lens == boxes[boxNum][-1]:
                #if its the last lens, and hasnt been found yet
                boxes[boxNum].append('{} {}'.format(label, labelNum))
                break
    else:
        boxes[boxNum].append('{} {}'.format(label, labelNum))

    return boxes

#Part 2
boxes = []
for i in range(256):
    boxes.append([])

for strings in inputs[0]:
    if '-' in strings:
        substring = strings.split('-')[0]
        boxes = removeLens(substring, boxes)
    else:
        substring, labelNum = strings.split('=')
        boxes = addLens(substring, labelNum, boxes)

total = 0
for ind, box in enumerate(boxes):
    for i, lens in enumerate(box):
        total += (ind + 1) * (i + 1) * int(lens[-1])

time_p2 = time.time() - start_time - time_p1
print("The solution to Part 2 is {} which took {:.4f} seconds to run".format(total, time_p2))

