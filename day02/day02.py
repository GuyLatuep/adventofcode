from collections import defaultdict
with open("day02/input.txt", "r") as file:
    text = file.read()
p1 = 0
p2 = 0
for game in text.split('\n'):
    ok = True
    id, game = game.split(':')
    maxdic = defaultdict(int)
    for round in game.split(';'):
      for cube in round.split(','):
         n, color = cube.split()
         n=int(n)
         maxdic[color] = max(maxdic[color], n)  
         if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
            ok = False
    score = 1
    for value in maxdic.values():
      score *= value
    p2 += score
    #print(score)
    if ok == True:
      p1 += int(id.split()[-1])     
print(p1)
print(p2)