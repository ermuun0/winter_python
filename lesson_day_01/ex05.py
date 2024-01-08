word = input('Enter word:')
index = len(word) - 1
while index >= 0:
    print(word[index])
    index = index - 1
fruit = 'banana'
count = fruit.count("a")
print(count)
str = 'X-DSPAM-Confidence:0.8475'
sindex = int(str.find('0')-1)
print(sindex)
tindex = int(str.find('5'))
float = float(str[sindex,tindex])
print(float)