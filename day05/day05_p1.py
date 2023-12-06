from collections import defaultdict

with open("day05/input.txt") as input:
    data = input.read()
    lines = data.strip().split("\n")

seeds = list(map(int, lines[0].split(" ")[1:]))
#load all maps
maps = []

i=2
while i < len(lines):
    maps.append([])

    i += 1
    while i < len(lines) and not lines[i] == "":
        dstStart, srcStart, rangeLen = map(int, lines[i].split())
        maps[-1].append((dstStart, srcStart, rangeLen))
        i += 1
    i += 1

def findLoc(seed):
    curNum = seed

    for m in maps:
        for dstStart, srcStart, rangeLen in m:
            if srcStart <= curNum < srcStart + rangeLen:
                curNum = dstStart + (curNum - srcStart)
                break
    return curNum

locs = []
for seed in seeds:
    loc = findLoc(seed)
    locs.append(loc)

print(min(locs))

