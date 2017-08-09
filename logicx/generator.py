import string 
from random import *  # This Random Moudle Added For Rand Int And Other
import os    # This Module Added For Get List Directory 
variable=list(string.ascii_letters)  # Convert Ascii Letter To List
operation=["'",'+',".","^"]  # Valid Operation

 # Generator Function Get Two Variable Number And Total Operation
 # Thi Function Create This String Randomly
def generator(var_num,total_num):
    index=0
    final_string=""
    while(True):
        var_index=randrange(0,var_num)
        op_index=randrange(0,4)
        op_index_not=randrange(1,4)
        if index%2==0:
            final_string=final_string+variable[var_index]
            index=index+1
        elif index%2==1:
            final_string=final_string+operation[op_index]
            index=index+1
            if operation[op_index]=="'":
                final_string=final_string+operation[op_index_not]
        if index>=total_num and final_string[len(final_string)-1] in variable:
            break
    return final_string

if __name__=="__main__":
    file_list=os.listdir()
    for i in range(len(file_list)):
        print(str(i+1)+"- "+file_list[i]+"\n")
    input_str=input("Please Enter One Of This File For Generate : \n")
    if int(input_str)<=len(file_list):
        file=open(file_list[int(input_str)-1],'w')
        input_number=input("Please Enter Number Of Variable in File : ")
        input_total=input("Please Enter Total Number Of Objects In Files : ")
        gen_function=generator(int(input_number),int(input_total))
        file.write(gen_function)
        file.close()
        print("File Writed!!")
        print("Generated Function : "+gen_function)
        
    else:
        "Wrong Files Number"
    
    
    

            
            
        
        
