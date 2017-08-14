def And(a,b):
    '''
    Logic And Function
    :param a: logic input
    :type a : int (in [0,1])
    :param b: logic input
    :type b: int (in [0,1])
    :return: a.b as bool
    '''
    if (a in [0,1] and b in [0,1]):
        return a and b
    else:
        print("Input Is Not Boolean")
        return None

def Or(a,b):
    '''
       Logic Or Function
       :param a: logic input
       :type a : int (in [0,1])
       :param b: logic input
       :type b: int (in [0,1])
       :return: a+b as bool
       '''
    if (a in [0,1] and b in [0,1]):
        return a or b
    else:
        print("Input Is Not Boolean")
        return None

def Xor(a,b):
    '''
       Logic Xor Function
       :param a: logic input
       :type a : int (in [0,1])
       :param b: logic input
       :type b: int (in [0,1])
       :return: a^b as bool
       '''
    if (a in [0,1] and b in [0,1]): 
        if (a == b):
            return 0
        else:
            return 1
    else:
        print("Input Is Not Boolean")
        return None
def Not(a):
    '''
       Logic Not Function
       :param a: logic input
       :type a : int (in [0,1])
       :return: not(a) as bool
       '''
    if a in [0,1]:
        if (a == 0):
            return 1
        else:
            return 0
    else:
        print("Input Is Not Boolean")
        return None
    
def Nand(a,b):
    '''
       Logic Nand Function
       :param a: logic input
       :type a : int (in [0,1])
       :param b: logic input
       :type b: int (in [0,1])
       :return: not(a.b)  as bool
       '''
    return Not(And(a,b))

def Nor(a,b):
    '''
       Logic NorFunction
       :param a: logic input
       :type a : int (in [0,1])
       :param b: logic input
       :type b: int (in [0,1])
       :return: not(a+b) as bool
       '''
    return Not(Or(a,b))

def Xnor(a,b):
    '''
       Logic Xnor Function
       :param a: logic input
       :type a : int (in [0,1])
       :param b: logic input
       :type b: int (in [0,1])
       :return: not(a^b) as bool
       '''
    return not(Xor(a,b))

