// Verilog model for OSU350_5P0V_25C; 
`timescale 1ns/1ns
module INV_1X(YB,A);
output YB;
input A;
assign YB = !A;
endmodule

