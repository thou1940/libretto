// Verilog model for HWN5; 
`timescale 1ns/1ns
module DFFHQx1(Q,D,CLK);
output reg Q;
input D;
input CLK;
always@(posedge CLK)begin
Q<=D;
end
end
endmodule

