data = open("data","r").read().split("\n\n")
valid = 0


def t1(byr):
    y = int(byr.replace("byr:",""))
    return True if y > 1919 and y < 2003 else False

def t2(ecl):
    c = ecl.replace("ecl:","")
    l = ["amb","blu","brn","gry","grn","hzl","oth"]
    return True if c in l else False

def t3(eyr):
    y = int(eyr.replace("eyr:",""))
    return True if y > 2019 and y < 2031 else False

def t4(hcl):
    h = hcl.replace("hcl:","")
    #print(h)
    if h[0] == "#" and len(h) == 7:
        return True
    else:
        return False

def t5(hgt):
    if hgt[ len(hgt) - 1 ] ==  "m":
        h = int(hgt.replace("hgt:","").replace("cm",""))
        return True if h > 149 and h < 194 else False
    else:
        h = int(hgt.replace("hgt:","").replace("in",""))
        return True if h > 58 and h < 77 else False

def t6(iyr):
    y = int(iyr.replace("iyr:",""))
    return True if y > 2009 and y < 2021 else False


def t7(pid): 
    return True if len(pid) == 13 else False





i = 0
while i < len(data):
    data[i] = data[i].replace("\n"," ")
    i += 1
del i

for content in data:
    pp = content.split()
    for i in pp:
        if "cid" in i:
            pp.remove(i)

    if len(pp) > 6:
        pp.sort()
        #print(pp)

        if t1(pp[0]) and t2(pp[1]) and t3(pp[2]) and t4(pp[3]) and t5(pp[4]) and t6(pp[5]) and t7(pp[6]):
            valid += 1

print(valid)
    
    
