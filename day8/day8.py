data = open("data","r").read().split("\n")
data = data[:(len(data)-1)]

accumulator = 0
been = []
run = 0 

def nop(arg):
    pass

def acc(arg):
    global accumulator
    accumulator += arg

def jmp(arg):
    global run
    run = run + arg -1

def do():
    global run
    global accumulator
    line = data[run].split()
    cmd = line[0]
    arg = int(line[1])
    
    #print(str(run) + " " + data[run] + " " + str(accumulator))

    global been
    
    if run in been:
        print("loop")
        return(-1)
    elif run == 635:
        print("res")
        return accumulator

    been.append(run)

    if cmd == "nop":
        nop(arg)        
    elif cmd == "acc":
        acc(arg)
    elif cmd == "jmp":
        jmp(arg)
        
    else:
        print("error")
        while True:
            pass
    run += 1
    do()
i = 0
while i<len(data):
    if data[i].split()[0] == "jmp":
        store = data[i]
        data[i] = "nop 0"
        #if int(do()) > -1:
        #    print(str(do()))
        do()
        data[i] = store
    i += 1

