// Vibhore Sagar
//Verilog Assignment 3
// adder.v, 137 Verilog Programming Assignment 
//iverilog -o adder adder.v 
//output: ./adder

//Eda playground Link: https://www.edaplayground.com/x/AQFV


module TestMod;                     // the "main" thing

   reg [4:0] X, Y;      // 5-bit X, Y to sum
   wire [4:0] Sum;        // 5-bit Sum to see as result
   wire Carry_out;             // like to know this as well from result of adder
   //c5 = carry out

   //instantiate the big adder module (giving X and Y as input, getting S and Carry_out as output)
   BigAdder B_a(X, Y, Sum, Carry_out);
   
   initial begin
    $display("Time  X               Y           sum         Carry Out");
    $display("------------------------------------------------");
    $monitor("   %0d  %d(%b)       %d(%b)   %d(%b)   %b", $time, X, X, Y, Y, S, S, Carry_out);
   end

   initial begin
     
     X = 1; Y=1; #1;
     X = 2; Y=5; #1;
     X = 10; Y=15; #1;
     X = 17; Y=19; #1;
     X = 1; Y=31; #1;
     X = 31; Y=31; #1;

   end
endmodule

module BigAdder(X, Y, Sum, Carry_out);
   input [4:0] X, Y;   // two 5-bit input items
   output [4:0] Sum;          // S should be similar
   output Carry_out;          // another output for a different size

   // declare temporary wires
   wire [3:0] Carry_in;

   // ... (get an instance of a full adder, C0 is 0)
   FullAdderMod FAM_0(X[0], Y[0],        1'b0, S[0], Carry_in[0]);
   FullAdderMod FAM_1(X[1], Y[1], Carry_in[0], S[1], Carry_in[1]);
   FullAdderMod FAM_2(X[2], Y[2], Carry_in[1], S[2], Carry_in[2]);
   FullAdderMod FAM_3(X[3], Y[3], Carry_in[2], S[3], Carry_in[3]);
   FullAdderMod FAM_4(X[4], Y[4], Carry_in[3], S[4], Carry_out);
endmodule

module FullAdderMod(X, Y, Carry_in, Sum, Carry_out); // single-bit adder module
   //... code the full adder according to the diagram above

   input X, Y, Carry_in;
   output Sum, Carry_out;

   //temp wires
   wire and_xy, and_xy2, xor_xy;

   xor(xor_xy, X, Y);
   xor(Sum, xor_xy, Carry_in);

   and(and_xy, Carry_in, xor_xy);
   and(and_xy2, X, Y);

   or(Carry_out, and_xy, and_xy2);
endmodule