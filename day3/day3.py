data = open("data","r").read().split()
xtravels = [1,3,5,7,1]
ytravels = [1,1,1,1,2]

i = 0
trees = []
while i<len(xtravels):

    xTrav = 0
    yTrav = 0
    
    path = ""
    width = len(data[0])

    while yTrav < len(data):
        path += data[yTrav][xTrav % width]
        xTrav += xtravels[i]
        yTrav += ytravels[i]


    trees.append(path.count("#")) 
    print(trees)
    i += 1
totTrees = 1
for j in trees:
    totTrees *= j
print(totTrees)

