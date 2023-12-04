from collections import defaultdict

with open("day04/input.txt") as input:
    data = input.read()
    lines = data.strip().split("\n")
p1 = 0
p2 = 0
Cards = defaultdict(int)

for i,line in enumerate(lines):
    Cards[i] += 1
    first, rest = line.split('|')
    gameNum, winningCard = first.split(':')
    winning_nums = [int(x) for x in winningCard.split()]
    card_nums = [int(x) for x in rest.split()]
    matches = len(set(winning_nums) & set(card_nums))
    for j in range(matches):
        Cards[i+1+j] += Cards[i]
    if matches > 0:
        p1 += 2**(matches-1) 
print('Part 1: ' + str(p1))
print('Part 2: ' + str(sum(Cards.values())))