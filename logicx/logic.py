def And(a,b):
    if (a in [0,1] and b in [0,1]):
        return a and b
    else:
        print("Input Is Not Boolean")
        return None

def Or(a,b):
    if (a in [0,1] and b in [0,1]):
        return a or b
    else:
        print("Input Is Not Boolean")
        return None

def Xor(a,b):
    if (a in [0,1] and b in [0,1]): 
        if (a == b):
            return 0
        else:
            return 1
    else:
        print("Input Is Not Boolean")
        return None
def Not(a):
    if a in [0,1]:
        if (a == 0):
            return 1
        else:
            return 0
    else:
        print("Input Is Not Boolean")
        return None
    
def Nand(a,b):
    return Not(And(a,b))

def Nor(a,b):
    return Not(Or(a,b))

def Xnor(a,b):
    return not(Xor(a,b))

