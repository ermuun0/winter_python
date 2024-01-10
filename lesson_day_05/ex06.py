fileName = input('File name: ')
if fileName == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    fhand = open(fileName)
    count = 0
    sum =0
    for line in fhand:
      if line.startswith('X-DSPAM-Confidence:'):
        print(line[-7:])
        count= count+1
        sum += float(line[-7:])
    print(count)
    print (sum)
    print(sum/count)