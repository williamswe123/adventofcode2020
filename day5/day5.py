def get(row,bsp):

    if len(bsp) == 0:
        return row
    
    s = bsp[0]
    bsp = bsp[1:]

    if s == "B" or s == "R":
        return get(row + pow(2,len(bsp)) , bsp )
    elif s == "F" or s == "L":
        return get(row,bsp)
    
taken = []
data = open("data","r").read().split()
for seat in data:
    row = seat[0:7]
    col = seat[7:]
    taken.append(get(0,row) * 8 + get(0,col))

taken.sort()

i = taken[1]
while i<len(taken)-1:
    if i not in taken:
        print(i)
    i += 1
