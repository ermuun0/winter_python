l = ['a', 'b' , 'c', 'd', 'e']
def chop(list):
    del list[-1]
    del list[0]
    return None
chop(l)
print (l)

