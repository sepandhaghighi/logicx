import string 
from random import *  # This Random Moudle Added For Rand Int And Other
import os    # This Module Added For Get List Directory 
variable=list(string.ascii_letters)  # Convert Ascii Letter To List
operation=["'",'+',".","^"]  # Valid Operation

# This Function Create Gate Generation
def Gate_Gen(gate_number,var_num,not_off=True):
    gate_index=0  # Gate Index That Increase In Loop
    gate_list=[] # Empty List Of Gate
    while(gate_index<gate_number):
        coin_1=randrange(0,2)  # Coin_1 For Var_1 Not Gate
        coin_2=randrange(0,2)   # Coin_2 For Var_2 Not Gate
        var_1=""  # Empty Var_1
        var_2=""  # Empty Var_2
        while(var_1==var_2):  # Generate Random Until Two Variable Be Different
            var_1=variable[randrange(0,var_num)]
            var_2=variable[randrange(0,var_num)]
        if not_off==False: # Check Not_False Argument
            if coin_1==1:
                var_1=var_1+"'"
            if coin_2==1:
                var_2=var_2+"'"
            
        op_index_not=randrange(1,4) # Operation Factor
        #coin_3=randrange(0,2)
        
        gate_list.append("("+var_1+operation[op_index_not]+var_2+")") # Create And Append One Gate At The End OF List
        gate_index=gate_index+1 # increase Gate_index
    return gate_list
# Generator Final String
def generator(gate_list,not_off=True):
    temp=gate_list # Copy OF The Input Gate List
    temp_2=[] # Empty List
    while(len(temp)>2): # Do This While Until We Have Two Object Process
        i=0 # Counter
        coin_not=randrange(0,2) # Random Number For Add Not At The End Of Each Paranteces
        if coin_not==1: # Condition Of Not Adding
            temp[i]=temp[i]+"'"  # Add Not To The First
        if len(temp)%2==0: # Even Length
            while((i+2)<=len(temp)):
                op_index=operation[randrange(1,4)] # Generate Random Operation (-Not In This Version)
                temp_2.append("("+temp[i]+op_index+temp[i+1]+")")
                i=i+2
        else:  # Odd Length
            while((i+2)<=len(temp)):
                op_index=operation[randrange(1,4)] # Generate Random Operation (- Not In This Version)
                temp_2.append("("+temp[i]+op_index+temp[i+1]+")") # merge tuple Of Two From Original List
                i=i+2 # Jump To Next Two
            temp_2.append(temp[len(temp)-1]) # Create New Gate List
        temp=temp_2 # Copy To First Temp
        temp_2=[] # Clear List
    return temp[1]+operation[randrange(1,4)]+temp[0] # merge Last Two Object And Return Last Object
            
            
                
                  
if __name__=="__main__":
    file_list=os.listdir()
    for i in range(len(file_list)):
        print(str(i+1)+"- "+file_list[i]+"\n")
    input_str=input("Please Enter One Of This File For Generate : \n")
    if int(input_str)<=len(file_list):
        file=open(file_list[int(input_str)-1],'w')
        gate_number=input("Please Enter Number Of 2-Input Gates in File : ")
        var_number=input("Please Enter Total Number Of Var in File")
        try:
            gate_form=Gate_Gen(int(gate_number),int(var_number))
            print(gate_form)
            gen_function=generator(gate_form)
            file.write(gen_function)
            file.close()
            print("Function : "+gen_function)
            print("Done!!")
        except:
            print("Wrong Number Inserted")
            file.close()
        
    else:
        "Wrong Files Number"
    
        
        
            
        
        
        
