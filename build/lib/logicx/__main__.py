from .VLSI import *
from .parser2 import *
import platform
from . import globals
from .generator_2 import *
import sys
import os
import doctest
def save_log(input_var_num,input_op_num,parser_perf_time,table_perf_time):
    '''
    This function save logicx log files
    :param input_var_num: number of input boolean expression variable
    :type input_var_num:int
    :param input_op_num: number of input boolean expression operator
    :type input_op_num:int
    :param parser_perf_time: parser elapsed time
    :type parser_perf_time:str
    :param table_perf_time: make table elapsed time
    :type table_perf_time:str
    :return: None
    '''
    today_date=datetime.datetime.today() # Today Date And Local Time For Saving In Performance Text File
    log_dir="logicx_Logs"
    if log_dir not in os.listdir():
        os.mkdir(log_dir)
    result_file = open(os.path.join(log_dir,"Parser_Perf_Result.txt"), "a")  # Open Result File
    result_file_2 = open(os.path.join(log_dir,"Table_Perf_Result.txt"), "a")
    result_file.write(
        file_name + " : ," + "Input Var Number: " + str(input_var_num) + " Input Operation Number: " + str(
            sum(input_op_num)) + " Elapsed Time: " + parser_perf_time + "  " + str(
            today_date) + " CPU: " + platform.processor() + "\n")  # Write Result In File
    result_file_2.write(
        file_name + " : ," + "Input Var Number: " + str(input_var_num) + " Input Operation Number: " + str(
            sum(input_op_num)) + " Elapsed Time: " + table_perf_time + "  " + str(
            today_date) + " CPU: " + platform.processor() + "\n")  # Write Result In File
    result_file.close()  # Close Parser Text File
    result_file_2.close()  # Close Table Maker File
def run(inputstring):
    '''
    This function apply  main operations on input expression
    :param inputstring: input expression
    :type inputstring : str
    :return: None
    '''
    input_var_num=input_num(inputstring)
    input_op_num=input_op(inputstring)
    globals.init()
    timer_1=time.perf_counter()   # Start Time Of Analysis
    parse_string(inputstring)
    timer_2=time.perf_counter()
    make_table()
    timer_3=time.perf_counter()
    # End Of Time Performance Counter
    parser_perf_time=str(timer_2-timer_1)+" Sec"
    table_perf_time=str(timer_3-timer_2)+" Sec"
    print("Parser Performance Time: "+parser_perf_time) # Print Time Performance
    print("Table Maker Performance Time: "+table_perf_time) # Print Time Performance
    make_script_files()
    print_result()
    save_log(input_var_num,input_op_num,parser_perf_time,table_perf_time)
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="GEN":
            run_generator()
        elif args[1].upper()=="TEST":
            doctest.testfile("test.py",verbose=True)
        else:
            file_name=args[1]
            file=open(file_name)
            inputstring=file.read()
            run(inputstring)
            file.close()
    else:
        print("[Error] In Parameters")
        sys.exit()


                        


       
