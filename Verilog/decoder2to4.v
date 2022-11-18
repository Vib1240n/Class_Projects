// (MY NAME)
// decoder2to4.v, 2-to-4 decoder, gate synthesis


module DecoderMod(i1, i0, o0, o1, o2, o3, o4, o5, o6, o7);  // module definition
   input i2, i1, i0;
   output o0, o1, o2, o3, o4, o5, o6, o7;

   wire not_i1, not_i0;

   not(not_i1, i1);
   not(not_i0, i0);
   not(not_i2, i2);
   
   and(o0, not_i2, not_i1, not_i2);
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

   DecoderMod my_decoder(i1, i0, o0, o1, o2, o3); 

   initial begin
      $display("Time  i2  i1  i0   o0  o1  o2  o3  o4  o5  o6  o7");
      $display("----  -----------   -----------------------------");
      $monitor("   %0d   %b   %b   %b    %b   %b   %b   %b   %b   %b   %b", $time, i2, i1, i0, o0, o1, o2, o3, o4, o5, o6, o7);
   end

   initial begin
      i2 = 0; i1 = 0; i0 = 0;  // i are 00
      #1;              // wait 1 simulation time unit/cycle
      i2 = 0; i1 = 0; i0 = 1;  // i are 01
      #1;              // wait 1 simulation time unit/cycle
      i2 = 0; i1 = 1; i0 = 0;  // i are 10
      #1;              // wait 1 simulation time unit/cycle
      i2 = 0; i1 = 1; i0 = 1;  // i are 11
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 0; i0 = 0;  // i back to 00
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 0; i0 = 1;  // i are 01
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 1; i0 = 0;  // i are 10
      #1;              // wait 1 simulation time unit/cycle
      i2 = 1; i1 = 1; i0 = 1;  // i are 11
   end

/* or, use always (forever) loop with delay to alter states
   always begin
      i0=0;
      #1;      // smallest delay
      i0=1;
      #1;
   end
   always begin
      i1=0;
      #2;      // larger delay (twice as much)
      i1=1;
      #2;
   end
   initial begin
      #4;
      $finish; // force-end forever loops
   end
*/

endmodule
