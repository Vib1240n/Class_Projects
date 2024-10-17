// (Vibhore Sagar)
// decoder3to8.v, 3-to-8 decoder, gate synthesis


module DecoderMod(i2, i1, i0, o0, o1, o2, o3, o4, o5, o6, o7);  // module definition
   input i2, i1, i0;
   output o0, o1, o2, o3, o4, o5, o6, o7;

   wire not_i2, not_i1, not_i0;

   not(not_i1, i1);
   not(not_i0, i0);
   not(not_i2, i2);
   
   and(o0, not_i2, not_i1, not_i0);
   and(o1, not_i2, not_i1,     i0);
   and(o2, not_i2,     i1, not_i0);
   and(o3, not_i2,     i1,     i0);
   and(o4, i2,     not_i1, not_i0);
   and(o5, i2,     not_i1,     i0);
   and(o6, i2,         i1, not_i0);
   and(o7, i2,         i1,     i0);
endmodule

module TestMod;           
   reg i2, i1, i0;            
   wire o0, o1, o2, o3, o4, o5, o6, o7;   

   DecoderMod my_decoder(i2, i1, i0, o0, o1, o2, o3, o4, o5, o6, o7); 

   initial begin
      $display("Time  i2  i1  i0   o0  o1  o2  o3  o4  o5  o6  o7");
      $display("----  -----------   -----------------------------");
      $monitor("   %0d   %b   %b   %b    %b   %b   %b   %b   %b   %b   %b   %b", $time, i2, i1, i0, o0, o1, o2, o3, o4, o5, o6, o7);
   end

   initial begin
      i2 = 0; i1 = 0; i0 = 0;  // i are 000
      #1;              // wait 1 simulation time unit/cycle
      i2 = 0; i1 = 0; i0 = 1;  // i are 001
      #1;              // wait 1 simulation time unit/cycle
      i2 = 0; i1 = 1; i0 = 0;  // i are 010
      #1;              // wait 1 simulation time unit/cycle
      i2 = 0; i1 = 1; i0 = 1;  // i are 011
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 0; i0 = 0;  // i are 100
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 0; i0 = 1;  // i are 101
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 1; i0 = 0;  // i are 110
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 1; i0 = 1;  // i are 111
   end
endmodule


//Link: https://www.edaplayground.com/x/6nD8