data = open("data","r").read().split()
data = [int(i) for i in data]

#print(data)

number = 25
while number < len(data):
    prev = data[number-25:number]
    #print(prev)
    #print(data[number])
    #print()
    b = False 
    for i in prev:
        for j in prev:
            #print(i+j)
            if i + j == data[number] and not i == j:
                b = True
    if not b:
        print(data[number])

    number += 1

