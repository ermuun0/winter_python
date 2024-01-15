import re
hand = open('mbox-short.txt')
word = input("Enter Word: ")
count = 0
for line in hand:
    line = line.strip()
    if re.search('^'+word, line):
        print(line)
        count = count +1
print(count)
    