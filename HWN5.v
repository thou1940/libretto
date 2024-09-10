// Verilog model for HWN5; 
`timescale 1ns/1ns
module INVx1(Y,A);
output Y;
input A;
assign Y = !A;
endmodule

