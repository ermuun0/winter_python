# while True:
#     line = input('>')
#     if line == 'done':
#         break
#     print(line)
# print('the end')
numbers = []
while True:
    try:
        line = input('Enter a number: ')
        if line == 'done':
            break
        number = int(line)
        numbers.append(number)
        
    except:
        print('Invalid Input')
 

#   while type(line[0] )== int:
      
#   if line == 'done':
      
#      break


print(sum(numbers))
print(len(numbers))
print(sum(numbers)/len(numbers))
print('The End!')