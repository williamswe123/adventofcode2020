data = open("data","r").read().split()
data = [int(i) for i in data]
data.sort()
#print(data)

Diffs = [0,0,0]

i = 0
while i < len(data) -1:
    print(data[i])
    diff = data[i+1] - data[i] - 1
    print("-- " + str(diff))
    Diffs[diff] += 1
    i += 1

print("1-diff * 3-diff: ")
for i in Diffs:
    i += 1

print((Diffs[0] + 1) * (Diffs[2] + 1))

