import re
def concatenate_integers(a, b):
    concatenated = str(a) + str(b)
    return int(concatenated)
sum = 0
text = open("day01/input.txt", "r")
for line in text:
    firstDiget = re.search(r'\d', line[::1]).group()[::1]
    lastDiget = re.search(r'\d', line[::-1]).group()[::-1]
    linenumber = concatenate_integers(firstDiget, lastDiget)
    sum = sum + linenumber
    print(linenumber)

print(sum)
