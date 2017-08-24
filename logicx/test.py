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
>>> temp=VLSI("(a+b)","test",len(globals.VLSIlist))
>>> print(temp)
VLSI((a+b))
>>> temp
VLSI_Object(Input_String=(a+b))
>>> temp.make_verilog()
>>> import os
>>> file=open(os.path.join("logicx_Verilog","Ftest.v"),"r")
>>> globals.VLSIlist.append(temp)
>>> make_table()
>>> globals.table
['0', '0', '1', '1', '1', '1', '1', '1']
>>> print_result()
test(ab)   Out
000   0
100   0
010   1
110   1
001   1
101   1
011   1
111   1
>>> temp=VLSI("((a+b).c)+(e+c).(a+c)","test2",len(globals.VLSIlist))
>>> print(temp)
VLSI(((a+b).c)+(e+c).(a+c))
>>> temp
VLSI_Object(Input_String=((a+b).c)+(e+c).(a+c))
>>> temp.make_verilog()
>>> file=open(os.path.join("logicx_Verilog","Ftest.v"),"r")
>>> globals.VLSIlist.append(temp)
>>> make_table()
>>> globals.table
['0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

'''