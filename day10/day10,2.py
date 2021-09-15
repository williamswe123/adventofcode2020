data = open("data","r").read().split()
data = [int(i) for i in data]
data.sort()

ways = 0

def rep(arg):
    print( data.index(arg) )

print( data.index(0) )
print(ways)
