import string
import os
from . import globals
valid_input=[1,0,True,False] # Valid Input For Boolean Functions
def input_num(input_str):
    '''
    This function calculate number of input expression variables
    :param input_str: input expression
    :type input_str:str
    :return: number of variables as int
    '''
    try:
        input_list=[]
        for i in input_str:
            if (i in string.ascii_letters) and (i not in input_list):
                input_list.append(i)
        return len(input_list)
    except:
        print("Please Pass logicx Object To Function")
        return None

def input_op(input_str):
    '''
    This Function Count Boolean Operation In Input String Separately
    :param input_str: input expression
    :type input_str:str
    :return: return number of each operation as a list [AND,OR,XOR,XNOR]
    '''
    try:
        counter=[0,0,0,0]
        input_list=[]
        for i in input_str:
            if i==".":
                counter[0]=counter[0]+1
            elif i=="+":
                counter[1]=counter[1]+1
            elif i=="^":
                counter[2]=counter[2]+1
            elif i=="'":
                counter[3]=counter[3]+1
        return counter   # Return List
    except:
        print("Error In Input")
        return None
                
            
def check_valid(input_string):
    '''
    This function check input expression validation ([A-Z]+['+^.()#!]
    :param input_str: input expression
    :type input_str:str
    :return: True if input is valid and False otherwise
    '''
    try:
        for i in input_string:
            if i not in string.ascii_letters+ string.digits +"'+^.() #!":
                return False
        return True
    except:
        print("Problem In Input")
        return None

def table_maker(obj):
    pass
def func_creator(obj):
    pass


def make_script_files():
    '''
    This function generate .scr files in logicx_Scripts folder
    :return: None
    '''
    if "logicx_Scripts" not in os.listdir():
        os.mkdir("logicx_Scripts")
    for t in globals.logicxlist:
        file_name = 'S' + t.packname.replace("#",'')
        verilog_name = 'F'+ t.packname.replace('#','')
        script_file=open(os.path.join("logicx_Scripts",file_name +'.scr'),"w")
        script_file.write('set power_preserve_rtl_hier_names "true"\n')
        script_file.write('analyze -format verilog { ../source/Verilogs/' + verilog_name + '.v' +'}\n')
        script_file.write('elaborate ' + verilog_name+'\n')
        script_file.write('link\n')
        script_file.write('uniquify -force\n')
        script_file.write('compile -map_effort medium\n')
        script_file.write('change_names -rules verilog -hierarchy\n')
        script_file.write('write -format verilog -hierarchy -output '+ '../netlist/' + verilog_name + '.v\n')
        script_file.write('uplevel #0 { report_power -analysis_effort low } > ../Power/' + verilog_name +'.txt\n')
        script_file.write('uplevel #0 { report_area -nosplit } > ../Area/'+ verilog_name +'.txt\n')
        script_file.close()
