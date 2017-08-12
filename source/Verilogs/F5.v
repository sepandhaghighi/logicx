module F5 (b , i , VV5V); 
input b , i;
output VV5V;
xor f0 (VV5V , b , i);
endmodule