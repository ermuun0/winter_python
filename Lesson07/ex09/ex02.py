fhand = open('mbox-short.txt')
word_dict = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        word_list=line.split(' ')
        # print (word_list)
        if len(word_list) >= 7:
            time = word_list[6]
            hour = time.split(':')
            # for number in hour:
            #     print(number)
            numbers= hour[0]
            word_dict[numbers] = word_dict.get(numbers, 0)+1
        # print (time)
print(word_dict)
for word in word_dict.items():
    number , count = word
    print(number, count) 