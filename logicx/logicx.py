from .functions import * # Outside Of The Class Functions
from .logic import *
import os
from . import globals
import time # Import Time Module For Counter Performance
import datetime # Import Date And Time For Saving Result

class funcObject:
    '''
    Basic object to handle logic functions
    It can either represent a single input function like Not, or dual input functions like And, Or
    '''
    def __init__(self,firstvar,outputvar,secondvar=-1,funct=Not):
        self.func = funct
        self.firstvarptr = firstvar
        self.secondvarptr = secondvar
        self.output = outputvar
        
    def function(self,c,d):
        '''
        Run the function using the values gived to the function
        :param c: input 1 binary
        :param d: input 2 binary
        :return: binary
        '''
        if (self.func != Not):
            return self.func(c,d)
    def Notfunction(self,ar):
        '''
        Run the Not function using the given value
        :param ar: input to be inverted
        :return: inverse of ar
        '''
        if (self.func == Not):
            return self.func(ar)
    def printobj(self):
        '''
        Describe the function in string
        :return: string containing description of function
        '''
        toprint = ''
        if (self.func == And):
            toprint = "And"
        elif (self.func == Or):
            toprint = "Or"
        elif (self.func == Xor):
            toprint = "Xor"

        if (self.func == Not):
            toprint = "Not"
        print('gate: ' + toprint)             
        
        
    
    

class logicx:

#    variables = []
#    func = []
#    inputs = []
#    wires = []

    packname = ''
    firstvar = -1
    secondvar = -1
    outputvar = -1

    
    def __init__(self,string,output,index):
        '''
           Initializer for the logicx class
           :param string: input string to be parsed
           :type string : str
           :param output: pointer to the variable containing the output value of this object
           :type output: int
           :param index: index of the logicx object, for it to be unique in case of replacing variables
           :type index: int
           '''
        if check_valid(string):
            self.inputs = []
            self.wires = []
            self.func = []
            self.variables = []
            
            self.input=string # Input String
            self.inputnum=input_num(string) # Add Input Number As Attribute
            #print(str(self.outputvar))
            #checking for variables and functions in the passed string

            
            self.varcounter = 0

            start = 0
            end = -1
            #start and end of each section
            
            cursor = 0
            clone = string
            clone.replace(" ","")
            #cloning input string


            ## !a + !(c+a.d)

            ## detecting and replacing NOTs with variables 
            while (1):
                symbolcounter = 0
                for i in range(0,len(clone)):
                    if clone[i] in "+.^!":
                        symbolcounter +=1
                if cursor == len(clone)-1:
                    break
                elif (clone[cursor] == "!"):
                    start = cursor+1
                    tempcursor = cursor +1
                    while (1):
                        if (tempcursor < len(clone)):
                            if clone[tempcursor] in "+.^":
                                break
                            tempcursor += 1
                        if (tempcursor == len(clone)):
                            break

                    end = tempcursor
                    tonot = self.handle_variable(clone[start:end])
                    self.inputs.append(clone[start:end])
                    self.packname = ('#%d' % index)+('#%d#' % self.varcounter)
                    self.varcounter += 1
                    if (symbolcounter == 1):
                        self.outputvar = self.handle_variable(output)
                        out = self.outputvar
                        self.packname = output
                    else:
                        out = self.handle_variable(self.packname)
                    self.wires.append(out)
                    tempfuncobject = funcObject(firstvar = tonot,outputvar = out)
                    self.func.append(tempfuncobject)
                    clone = clone[0:start-1] + self.packname + clone[end:]
                cursor += 1

            cursor = 0
            start = 0
            while (1):
                symbolcounter = 0
                for i in range(0,len(clone)):
                    if clone[i] in "+.^":
                        symbolcounter +=1
                if cursor == len(clone) - 1:
                    break
                elif clone[cursor] in "+.^":
                    if (clone[cursor] == '+'):
                        tempfunc = Or
                    elif (clone[cursor] == '.'):
                        tempfunc = And
                    elif (clone[cursor] == '^'):
                        tempfunc = Xor
                    else:
                        tempfunc = And
                    
                    end = cursor
                    #detect variable
                    temp1 = clone[start:end]
                    temp = clone[start:end]
                    if (self.count_sharps(temp) <= 2):
                        self.inputs.append(temp)
                    tempcursor = cursor + 1
                    while (clone[tempcursor] not in "+.^" and tempcursor != len(clone)-1):
                        tempcursor += 1
                    if (tempcursor == len(clone) -1):
                        tempcursor += 1
                    temp2 = clone[end+1:tempcursor]
                    temp = temp2
                    if (self.count_sharps(temp) <= 2):
                        self.inputs.append(temp)
                    self.packname = ('#%d' % index)+('#%d#' % self.varcounter)
                    self.varcounter+=1
                    if symbolcounter == 1:
                        self.outputvar = self.handle_variable(output)
                        out = self.outputvar
                        self.packname = output
                    else:
                        out = self.handle_variable(self.packname)
                        self.wires.append(out)
                    
                    first = self.handle_variable(temp1)
                    second = self.handle_variable(temp2)
                    
                    tempfuncobject = funcObject(first,out,second,tempfunc)
                    self.func.append(tempfuncobject)
                    clone = clone[0:start] + self.packname + clone[tempcursor:]

                    cursor = 0

                cursor += 1
            #if (output[0] == '#'):
#                output = 'V'+output
            self.inputs.append(output)
                                
                    
           
        ##else:
##            print("Please Enter Valid String")
    def handle_variable(self,string):
        '''
           Handle Variable function
           this function is used to handle variables that is found in a string.
           the new variable name is searched in the list of current variables, if there are any hits,
           the variable is marked as the found variable, and if not a new variable is created with the initial value of 0
           '''
        for i in range(0,len(globals.varlist.strlist)):
            if (string == globals.varlist.strlist[i]):
                self.variables.append(i)
                return len(self.variables)-1
        if (not('#' in string)):
            globals.inputs.ptrlist.append(len(globals.varlist.strlist))
            globals.inputs.strlist.append(string)
        globals.varlist.strlist.append(string)
        globals.varlist.varlist.append(0)
        self.variables.append(len(globals.varlist.varlist) - 1)
        return len(self.variables) - 1
    def count_sharps(self,string):
        '''
           Function for counting the number of times '#' is repeated in a string
           '''
        counter = 0
        for i in range(0,len(string)):
            if (string[i] == '#'):
                counter += 1
        return counter
    
    def __str__(self):
        #This Function Is For Showing the Object In Print Format
        return "logicx("+self.input+")"
    def __repr__(self):
        # Representing logicx Object
        return "logicx_Object(Input_String="+self.input+")"

    def function(self):
        '''
           Running the function binded to the logicx object with given inputs from self.variables array
           '''
        result = 0
        self.make_verilog()
        for i in range(0,len(self.func)):
            temp = self.func[i]
            in1 = self.variables[temp.firstvarptr]
            out = self.variables[temp.output]
            if (temp.func != Not):
                globals.varlist.varlist[out] = temp.function(globals.varlist.varlist[in1],globals.varlist.varlist[self.variables[temp.secondvarptr]])
            else:
                globals.varlist.varlist[out] = temp.Notfunction(globals.varlist.varlist[in1])
        return 1

    def make_verilog(self):
        '''
           Make Verilog file function
           creates a text file describing the logicx object using Verilog language
           this verilog file will be next used in the scripts
           '''
        file_name = 'F' + self.packname.replace("#",'')
        dir=os.listdir()
        if "logicx_Verilog" not in dir:
            os.mkdir("logicx_Verilog")
        verilog_file=open(os.path.join("logicx_Verilog" ,file_name +'.v'),"w")
        verilog_file.write('module ' + file_name + ' (')
        for v in range(0,len(self.inputs)):
            if (v != 0):
                 verilog_file.write(' , ')
            varname = self.inputs[v]
            if ('#' in varname):
                varname = 'V' + varname.replace('#','V')
            verilog_file.write(varname)
        verilog_file.write('); \n')
        for v in range(0,len(self.inputs)-1):
            if (v == 0):
                verilog_file.write('input ')
            else:
                verilog_file.write(' , ')
            varname = self.inputs[v]
            if ('#' in varname):
                varname = 'V' + varname.replace('#','V')
            verilog_file.write(varname)

        verilog_file.write(';\noutput ' + 'V' + self.inputs[len(self.inputs)-1].replace('#','V') + ';\n')
        if (len(self.wires) != 0):
            verilog_file.write('wire ')
            for w in range(0,len(self.wires)):
                if (w != 0):
                    verilog_file.write(' , ')
                verilog_file.write('W'+globals.varlist.strlist[self.variables[self.wires[w]]].replace('#','W'))

            verilog_file.write(';\n\n')

        
        for i in range(0,len(self.func)):

            firstflag = -1
            secondflag = -1
            outflag = -1

            
            f = self.func[i]
            outstr = globals.varlist.strlist[self.variables[f.output]]
            firststr = globals.varlist.strlist[self.variables[f.firstvarptr]]
            secondstr = f.secondvarptr
            if (secondstr != -1):
                secondstr = globals.varlist.strlist[self.variables[secondstr]]
            else:
                secondstr = "~"
            for j in self.inputs:
                if (outstr == j):
                    outstr = 'V'+outstr.replace('#','V')
                    outflag = 1
                if (firststr == j):
                    if ('#' in firststr):
                        firststr = 'V'+firststr.replace('#','V')
                    firstflag = 1
                if (secondstr == j):
                    if ('#' in secondstr):
                        secondstr = 'V'+secondstr.replace('#','V')
                    secondflag = 1

            if (firstflag != 1):
                firststr = 'W' + firststr.replace('#','W')
            if (secondflag != 1):
                secondstr = 'W' + secondstr.replace('#','W')
            if (outflag != 1):
                if (outstr == self.inputs[len(self.inputs)-1]):
                    outstr = 'V' + outstr.replace('#','W')
                else:
                    outstr = 'W' + outstr.replace('#','W')

            if (f.func == And):
                verilog_file.write(('and f%d ('% i) + outstr + ' , ' + firststr + ' , ' + secondstr + ');\n')  
            elif (f.func == Or):
                verilog_file.write(('or f%d ('% i) + outstr + ' , ' + firststr + ' , ' + secondstr + ');\n')
            elif (f.func == Xor):
                verilog_file.write(('xor f%d ('% i) + outstr + ' , ' + firststr + ' , ' + secondstr + ');\n')
            elif (f.func == Not):
                verilog_file.write(('not f%d ('% i) + outstr + ' , ' + firststr +  ');\n')
               
        verilog_file.write('endmodule')
        verilog_file.close()

        
    
    
