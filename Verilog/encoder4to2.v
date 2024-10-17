// (MY NAME)
// encoder4to2.v, 4-to-2 encoder, gate synthesis

module EncoderMod(i0, i1, i2, i3, o1, o0);
   input i0, i1, i2, i3;
   output o1, o0;

   or(o1, i2, i3);
   or(o0, i1, i3);
endmodule

module TestMod;
   reg i0, i1, i2, i3;
   wire o1, o0;

   EncoderMod my_encoder(i0, i1, i2, i3, o1, o0);

   initial begin
      $display("Time  i0  i1  i2  i3   o1  o0");
      $display("----  --------------   ------");
      $monitor("   %0d   %b   %b   %b   %b    %b   %b",
         $time, i0, i1, i2, i3, o1, o0);
   end

   initial begin
      i0 = 1; i1 = 0; i2 = 0; i3 = 0;   // initially 1000
      #1;                               // wait 1 cycle
      i0 = 0; i1 = 1; i2 = 0; i3 = 0;   // becomes 0100
      #1;                               // wait 1 cycle
      i0 = 0; i1 = 0; i2 = 1; i3 = 0;   // becomes 0010
      #1;                               // wait 1 cycle
      i0 = 0; i1 = 0; i2 = 0; i3 = 1;   // becomes 0001
      #1;                               // wait 1 cycle
      i0 = 1; i1 = 0; i2 = 0; i3 = 0;   // back to 1000
      #1;                               // wait 1 cycle
      i0 = 0; i1 = 1; i2 = 0; i3 = 0;   // becomes 0100
      #1;                               // wait 1 cycle
      i0 = 0; i1 = 0; i2 = 1; i3 = 0;   // becomes 0010
      #1;                               // wait 1 cycle
      i0 = 0; i1 = 0; i2 = 0; i3 = 1;   // becomes 0001
   end
endmodule
