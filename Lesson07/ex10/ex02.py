import re
hand = open('mbox-short.txt')
count = 0
summary_list = []
for line in hand:
    line = line.strip()
    x = re.findall("^New Revision: ([0-9]+)", line)
   
    if len (x) > 0:
        for i in range(0, len(x)):
            x[i] = int(x[i])
            summary_list.append(x[i])
            
        # print(x)
        count = count +1
print(sum(summary_list)/count)