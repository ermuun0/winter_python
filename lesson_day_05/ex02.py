unique_words = []
fhand = open('romeo.txt')
for line in fhand :
    t = line.split(' ')
    for word in t:
        if word not in unique_words:
         unique_words.append(word)
print (unique_words)
