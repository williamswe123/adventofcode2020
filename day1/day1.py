data = open("data","r").read().split()

for i in data:
    for j in data:
        for h in data:
            if int(i) + int(j) + int(h) == 2020:
                print(int(i)*int(j)*int(h))


