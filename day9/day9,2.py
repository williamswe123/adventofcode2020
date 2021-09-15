data = open("data","r").read().split()
data = [int(i) for i in data]

hack = 15690279

i = 0
while i < len(data)-1:
    j = i+1
    while j < len(data):
        l = data[i:j]
        if sum(l) == hack:
            l.sort()
            print(l)
        j += 1 
    i += 1

