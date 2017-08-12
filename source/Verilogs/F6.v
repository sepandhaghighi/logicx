module F6 (VV4V' , VV5V , VV6V); 
input VV4V' , VV5V;
output VV6V;
xor f0 (VV6V , VV4V' , VV5V);
endmodule