data = open("data","r").read().split("\n\n")
data = data[:len(data)-1]
q = "abcdefghijklmnopqrstuvwxyz"

tot = 0
group = data[0]
for group in data:
    a = 0
    members = group.count("\n") +1
    for c in q:
        if group.count(c) == members:
            a += 1
    tot += a
    print(members)

print(tot)
