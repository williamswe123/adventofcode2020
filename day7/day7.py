data = open("data","r").read().split("\n")
data = data[:len(data)-1]

rules = dict()
posBags = 0

for rule in data:
    rule = rule.replace(".","").replace("bags","").replace("bag","").split(" contain ")
    key = rule[0]
    contains = rule[1]
    rules[key] = contains 
print(rules.get("dark lavender "))
def contShinyGold(bag):
    if "shiny gold" in rules.get(bag):
        return True
    elif "no other" in rules.get(bag):
        return False
    else:
        cont = rules.get(bag).split(",")
        i = 0
        while i<len(cont):
            cont[i] = cont[i].split()[1:]
            cont[i] = cont[i][0] + " " + cont[i][1]
            i += 1
        boolean = False
        print(cont)
        for b in cont: 
            print(rules.get(b))

            boolean = boolean or contShinyGold(b + " ")
        return boolean

for bag in rules:
    posBags += 1 if contShinyGold(bag) else 0
       
print(posBags)


    
