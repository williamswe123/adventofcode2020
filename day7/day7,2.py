data = open("data","r").read().split("\n")
data = data[:len(data)-1]

rules = dict()
posBags = 0

for rule in data:
    rule = rule.replace(".","").replace("bags","").replace("bag","").split(" contain ")
    key = rule[0]
    contains = rule[1]
    rules[key] = contains 

indent = ""
def contShinyGold(bag):
    if "no other" in rules.get(bag):
        return 1

    cont = rules.get(bag)
    cont = cont[:(len(cont))].split(", ")
    print(bag)
    print(rules.get(bag))
    print(cont)
    buy = 1
    
    for b in cont:
        buy += int(b[0]) * (contShinyGold(b[2:]) )
    return buy 

 
print(contShinyGold("shiny gold ")-1)


    
