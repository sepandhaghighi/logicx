module F3 (VV1V , VV2V , VV3V); 
input VV1V , VV2V;
output VV3V;
xor f0 (VV3V , VV1V , VV2V);
endmodule