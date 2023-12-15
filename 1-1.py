#advent of code day 1, number 1
import csv
import re
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, "input-1-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0])

'''
#for problem 1 day 1
value = 0
for x in range(len(inputs)):
    nums = list(filter(lambda i: i.isdigit(), inputs[x]))
    
    if len(nums) == 1:
        value += int(nums[0]) * 11
        #print(nums, int(nums[0]) * 11)
    else:
        value += int(nums[0]) * 10 + int(nums[-1])
        #print(nums, int(nums[0]) * 10 + int(nums[-1]))

print(value)
'''

#for problem 2, day 1
value = 0
for x in range(len(inputs)):
    key = inputs[x]
    words = ['one','two','three','four','five','six','seven','eight','nine']
    matches = []
    mdict = {}
    for word in words:
        if word in key:
            found = [m.start() for m in re.finditer(word,key)]
            for w in found:
                matches.append(w)
                mdict[w] = word
    nums = list(filter(lambda i: i.isdigit(), key))     
    print(nums)
    ndict = {}
    for num in nums:
        nfound = [n.start() for n in re.finditer(num, key)]
        for n in nfound:
            matches.append(n)
            ndict[n] = num


    matches.sort()
    
    word_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

    if matches[0] in mdict:
        first = word_dict[mdict[matches[0]]]
    elif matches[0] in ndict:
        first = int(ndict[matches[0]])

    if matches[-1] in mdict:
        last = word_dict[mdict[matches[-1]]]
    elif matches[-1] in ndict:
        last = int(ndict[matches[-1]])

    value += int(first) * 10 + int(last)

    print(matches[0], matches[-1], mdict, ndict, key, int(first) * 10 + int(last))

print(value)
    






    
    