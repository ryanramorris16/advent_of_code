#advent of code day 3, number 1
import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, r"2023 Inputs/input-3-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0])
        
#print(inputs)

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '=', '+', '/', '-']
ast = []
sym_loc = []
starts = []
ends = []

#first find all symbols
for x in range(len(inputs)):
    line = inputs[x]
    for y in range(len(line)):
        if line[y] in symbols:
            sym_loc.append([x, y])   
        if line[y] == '*':
            ast.append([x,y])    
        if line[y].isdigit() and y == 0:
            starts.append([x, y])
        elif line[y].isdigit() and y == len(line)-1:
            ends.append([x, y])
        if y != 0:
            if line[y].isdigit() and not line[y-1].isdigit():
                #print(line[y - 1], line[y])
                starts.append([x, y])
        if y != len(line)-1:
            if line[y].isdigit() and not line[y + 1].isdigit():
                ends.append([x,y])
                # print(line[y + 1], line[y])

''' #part 1
total = 0
for x in range(len(starts)):
    start_row = starts[x][0]
    start_col = starts[x][1]
    end_row = ends[x][0]
    end_col = ends[x][1]
    for rows in range(start_row - 1, start_row + 2):
        for cols in range(start_col - 1, end_col + 2):
            #if [rows, cols] in sym_loc: #part 1
            #    number = 0
            #    for digit in range(0, (end_col - start_col) + 1):
            #        number += int(inputs[start_row][start_col + digit]) * (10 ** (int(end_col) - int(start_col) - digit))
            #    total += number  
'''

#part 2
total = 0
for x in range(len(ast)):
    ast_row = ast[x][0]
    ast_col = ast[x][1]
    times = 0
    for rows in range(ast_row - 1, ast_row + 2):
        for cols in range(ast_col - 1, ast_col + 2):
            if [rows, cols] in starts or [rows, cols] in ends:
                if times == 0:
                    n1 = 0
                    if [rows, cols] in starts:
                        index = starts.index([rows, cols])
                    elif [rows, cols] in ends:
                        index = ends.index([rows, cols])
                    row_cur = starts[index][0]
                    start_col = starts[index][1]
                    end_col = ends[index][1]
                    for digit in range(0, (end_col - start_col) + 1):
                        n1 += int(inputs[row_cur][start_col + digit]) * (10 ** (int(end_col) - int(start_col) - digit))
                    times = 1
                    del starts[index]
                    del ends[index]
                    #print(row_cur, start_col, n1)
                elif times == 1:
                    n2 = 0
                    if [rows, cols] in starts:
                        index = starts.index([rows, cols])
                    elif [rows, cols] in ends:
                        index = ends.index([rows, cols])
                    row_cur = starts[index][0]
                    start_col = starts[index][1]
                    end_col = ends[index][1]
                    for digit in range(0, (end_col - start_col) + 1):
                        n2 += int(inputs[row_cur][start_col + digit]) * (10 ** (int(end_col) - int(start_col) - digit))
                    times = 0 
                    del starts[index]
                    del ends[index]
                    total += n1 * n2
                    #print(n1,n2)

   

print(total)
