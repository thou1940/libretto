// Verilog model for OSU350_5P0V_25C; 
`timescale 1ns/1ns
module DFF_1X(Q,DATA,CLK);
output reg Q;
input DATA;
input CLK;
always@(posedge CLK)begin
Q<=DATA;
end
end
endmodule

