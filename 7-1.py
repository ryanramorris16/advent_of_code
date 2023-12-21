#advent of code day 7
import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []

with open(os.path.join(__location__, r"2023 Inputs/input-7-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row[0])

hands = []
bets = []
for i in inputs:
    hands.append(i.split(' ')[0])
    bets.append(i.split(' ')[1])

#part 1 - J:11, part 2 - J:1 and moved to end
cards = {"A":14, "K":13, "Q":12, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2, "J":1}

def read(hand):
    #takes a single hand and reads it, outputs a read rank from 1 (worst) to 7 (best)
    #print(hand)
    rank = 1
    trip = 0
    pair = 0
    for card in cards:
        count = hand.count(card)
        if card != "J":
            if count == 5:
                rank = 7
                break
            elif count == 4:
                rank = 6
                #break      #can break in part 1, not part 2
            elif count == 3:
                if pair == 0:
                    rank = 4
                    trip = 1
                if pair == 1:
                    rank = 5
                    #break      #can break in part 1, not part 2
            elif count == 2:
                if trip == 0 and pair == 1:
                    rank = 3
                    #break      #can break in part 1, not part 2
                elif trip == 0 and pair == 0:
                    rank = 2
                    pair = 1
                elif trip == 1:
                    rank = 5
                    #break      #can break in part 1, not part 2
        else:
            j_count = hand.count(card)
            #change rank of hand depending on current rank and how many jack(jokers)
            if j_count == 1 and rank != 6 and rank != 1:
                rank += 2
            elif j_count == 1 and (rank == 6 or rank == 1):
                rank += 1
            elif j_count == 2 and rank == 1:
                rank += 3
            elif j_count == 2 and rank == 2:
                rank += 4
            elif j_count == 2 and rank == 4:
                rank += 3
            elif j_count == 3:
                rank += 5
            elif j_count >= 4:
                rank = 7
            

    subrank = []
    for card in hand:
        subrank.append(cards.get(card))


    return rank, subrank

def sort(hands, bets):
    #taks in hands and bets to sort them based on rank and then by cards
    ranks = []
    sranks = []
    for hand in hands:
        ranks.append(read(hand)[0])
        sranks.append(read(hand)[1])

    sort1 = sorted(zip(sranks,ranks,hands,bets), reverse=True)
    sort2 = sorted(sort1, key= lambda x : x[1], reverse=True)

    #print(sort2)

    total = 0
    for i in range(len(sort2)):
        total += (int(sort2[i][3]) * (len(sort2) - i))

    return total

print(sort(hands,bets))

#print(read("JJJJ4"))