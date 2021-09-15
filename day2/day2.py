data = open("data","r").read().split()

amount = 0

i=0
while i<len(data):
    pos1 = int( data[i].split("-")[0] )-1
    pos2 = int( data[i].split("-")[1] )-1
    i += 1

    char = data[i].replace(':','')
    
    i += 1

    pwa = data[i]
    
    i += 1
    if (pwa[pos1] == char) ^ (pwa[pos2] == char):
        amount += 1
        print(data[i-1])
print(amount)
