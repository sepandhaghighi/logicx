'''
>>> from logicx import *
>>> And(1,0)
0
>>> And(1,1)
1
>>> And(0,1)
0
>>> And(0,0)
0
>>> Or(1,1)
1
>>> Or(1,0)
1
>>> Or(0,0)
0
>>> Or(0,1)
1
>>> Xor(1,1)
0
>>> Xor(1,0)
1
>>> Xor(0,1)
1
>>> Xor(0,0)
0
>>> Not(1)
0
>>> Not(0)
1
>>> Nand(0,0)
1
>>> Nand(0,1)
1
>>> Nand(1,0)
1
>>> Nand(1,1)
0
>>> Nor(0,1)
0
>>> Nor(1,0)
0
>>> Nor(1,1)
0
>>> from random import *
>>> seed(2)
>>> Gate_Gen(3,2)
['(a+b)', '(a^b)', '(b^a)']
>>> seed(2)
>>> Gate_Gen(10,10)
['(b+f)', '(j^d)', '(i^f)', '(f.h)', '(i^c)', '(d+a)', '(c^i)', '(h^g)', '(f+h)', '(i.d)']
>>> seed(2)
>>> generator(['(b+f)', '(j^d)', '(i^f)', '(f.h)', '(i^c)', '(d+a)', '(c^i)', '(h^g)', '(f+h)', '(i.d)'])
"((f+h)^(i.d))+((((b+f)+(j^d))'.((i^f)+(f.h)))^(((i^c).(d+a))^((c^i)+(h^g))))"
>>> seed(2)
>>> generator(['(b+f)', '(j^d)', '(i^f)', '(f.h)', '(i^c)', '(d+a)', '(c^i)', '(h^g)', '(f+h)', '(i.d)'],not_off=False)
"((f+h)^(i.d))+((((b+f)+(j^d))'.((i^f)+(f.h)))^(((i^c).(d+a))^((c^i)+(h^g))))"
>>> check_valid("((f+h)^(i.d))+((((b+f)+(j^d))'.((i^f)+(f.h)))^(((i^c).(d+a))^((c^i)+(h^g))))")
True
>>> check_valid("(f&2@q)")
False
>>> input_op("((f+h)^(i.d))^((((b+f)'.(j^d))'.((i^f)^(f.h)))'.(((i^c)^(d+a)).((c^i).(h^g))))")
[7, 3, 9, 3]
>>> input_op("((f+h)^(i.d))+((((b+f)+(j^d))'.((i^f)+(f.h)))^(((i^c).(d+a))^((c^i)+(h^g))))")
[4, 7, 8, 1]
>>> input_num("f+f+f+f")
1
>>> input_num("d+d+s+x+w")
4
>>> input_num("((f+h)^(i.d))+((((b+f)+(j^d))'.((i^f)+(f.h)))^(((i^c).(d+a))^((c^i)+(h^g))))")
9
>>> globals.init()
>>> tempobject = logicx("(a+b)",'#%d#' % 1,len(globals.logicxlist))
>>> globals.logicxlist.append(tempobject)
>>> make_table()
>>> print_result()
(ab)   Out
00   0
10   1
01   1
11   1
>>> globals.table
['0', '1', '1', '1']
>>> print(tempobject)
logicx((a+b))
>>> tempobject
logicx_Object(Input_String=(a+b))
>>> tempobject.make_verilog()
>>> tempobject = logicx("(a+b).(c+d)",'#%d#' % 2,len(globals.logicxlist))
>>> globals.logicxlist.append(tempobject)
>>> make_table()
>>> print_result()
(ab)(cd)   Out
0000   0
1000   1
0100   1
1100   1
0010   0
1010   0
0110   0
1110   0
0001   0
1001   1
0101   1
1101   1
0011   1
1011   1
0111   1
1111   1
>>> globals.table
['0', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
>>> print(tempobject)
logicx((a+b).(c+d))
>>> tempobject
logicx_Object(Input_String=(a+b).(c+d))
>>> tempobject.make_verilog()
>>> import os
>>> file_1=open(os.path.join("logicx_Verilog","F1.v"),"r")
>>> print(file_1.readlines())
['module F1 ((a , b) , VV1V); \n', 'input (a , b);\n', 'output VV1V;\n', 'or f0 (VV1V , (a , b));\n', 'endmodule']
>>> file_2=open(os.path.join("logicx_Verilog","F2.v"),"r")
>>> print(file_2.readlines())
['module F2 ((a , b) , (c , d) , VV2V); \n', 'input (a , b) , (c , d);\n', 'output VV2V;\n', 'wire WW1W0W , WW1W1W;\n', '\n', 'or f0 (WW1W0W , (a , b));\n', 'and f1 (WW1W1W , WW1W0W , (c);\n', 'or f2 (VV2V , WW1W1W , d));\n', 'endmodule']
>>> make_script_files()
>>> file_3=open(os.path.join("logicx_Scripts","S1.scr"),"r")
>>> print(file_3.readlines())
['set power_preserve_rtl_hier_names "true"\n', 'analyze -format verilog { ../source/Verilogs/F1.v}\n', 'elaborate F1\n', 'link\n', 'uniquify -force\n', 'compile -map_effort medium\n', 'change_names -rules verilog -hierarchy\n', 'write -format verilog -hierarchy -output ../netlist/F1.v\n', 'uplevel #0 { report_power -analysis_effort low } > ../Power/F1.txt\n', 'uplevel #0 { report_area -nosplit } > ../Area/F1.txt\n']
>>> file_4=open(os.path.join("logicx_Scripts","S2.scr"),"r")
>>> print(file_4.readlines())
['set power_preserve_rtl_hier_names "true"\n', 'analyze -format verilog { ../source/Verilogs/F2.v}\n', 'elaborate F2\n', 'link\n', 'uniquify -force\n', 'compile -map_effort medium\n', 'change_names -rules verilog -hierarchy\n', 'write -format verilog -hierarchy -output ../netlist/F2.v\n', 'uplevel #0 { report_power -analysis_effort low } > ../Power/F2.txt\n', 'uplevel #0 { report_area -nosplit } > ../Area/F2.txt\n']

'''