from VLSI import *
import globals

def make_table():
    for counter in range(0,2**(len(globals.inputs.strlist))):
        temp = counter
        for i in range(0,len(globals.inputs.strlist)):
            globals.varlist.varlist[globals.inputs.ptrlist[i]] = int(temp%2)
            temp =int(temp/ 2)

        globals.table.append(calculate_result())
        counter+=1

def print_result():
    outstr = ''
    for i in globals.inputs.strlist:
        outstr += i
    print (outstr+ '   Out') 

    for counter in range(0,2**(len(globals.inputs.strlist))):
        #print('number of inputs: ' + str(len(globals.inputs.strlist)))
        temp = counter
        outstr = ''
        for i in range(0,len(globals.inputs.strlist)):
            outstr += str(temp%2)
            temp = int(temp/2)

        outstr += '   ' + globals.table[counter]
        print(outstr)

def calculate_result():
    for temp in globals.VLSIlist:
        while (not temp.function()):
 #           output = temp.func[len(temp.func)-1].output
            pass
    temp = globals.VLSIlist[len(globals.VLSIlist)-1]
    return str(globals.varlist.varlist[temp.variables[temp.func[len(temp.func)-1].output]])
        



def parse_string(inputstring):
    
    start = -2
    end = -1
    indexcounter = 0
    i = 0
    j = 0

    temp = inputstring
    temp.replace(" ",'')

    while (i < len(temp)):
    
        if (temp[i] == ')'):
            end = i
            j = i
            while (j >= 0):
                if (temp[j] == '('):
                    start = j
                    break
                else:
                    j-=1
            
            if (start < 0):
                break
        elif (i == len(temp) -1):
            start = 0
            end = len(temp) - 1
            indexcounter += 1
            packname = ('#%d#' % indexcounter)
            tempobject = VLSI(temp,packname,len(globals.VLSIlist))
            globals.VLSIlist.append(tempobject)
            break
            
        
        if (start >= 0):        
            indexcounter+=1
            temp1 = temp[start+1:end]
            packname = ('#%d#' % indexcounter) #    (a+b) -> #indexcounter# and is saved as a var 
            tempobject = VLSI(temp1,packname,len(globals.VLSIlist))
            globals.VLSIlist.append(tempobject)
            temp = temp[:start]+('#%d#' % (indexcounter)) + temp[end+1:]
            start = -2
            end = -1
            i = 0
    
        i+=1
