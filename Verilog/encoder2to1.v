// (MY NAME)
// encoder2to1.v, 2-to-1 encoder, gate synthesis


module EncoderMod(i0, i1, i2, i3, i4, i5, i6, i7, o1, o2, o3);
   input i0, i1, i2, i3, i4, i5, i6, i7;
   output o1, o2, o3;

   assign o = i1;
endmodule

module TestMod;
   reg i0, i1, i2, i3, i4, i5, i6, i7;
   wire o1, o2, o3;

   EncoderMod my_encoder(i0, i1, i2, i3, i4, i5, i6, i7, o1, o2, o3);

   initial begin
      $display("Time  i1 i2 i3 i4 i5 i6 i7    o1 o2 o3");
      $display("----  --------------------   ---------");
      $monitor("   %0d   %b   %b   %b   %b   %b   %b   %b   %b    %b   %b   %b", $time, i0, i1, i2, i3, i4, i5, i6, i7, o1, o2, o3);
   end

   initial begin
      i0 = 1; i1=0; i2=0; i3=0; i4=0; i5=0; i6=0; i7=0;   // initially 10
      #1;   
      i0 = 0; i1=1; i2=0; i3=0; i4=0; i5=0; i6=0; i7=0;   // change to 01
      #1;               
      i0 = 0; i1=0; i2=1; i3=0; i4=0; i5=0; i6=0; i7=0;   // back to 10
      #1;               
      i0 = 0; i1=0; i2=0; i3=1; i4=0; i5=0; i6=0; i7=0;
      #1
      i0 = 0; i1=0; i2=0; i3=0; i4=1; i5=0; i6=0; i7=0;   // change to 01
      #1
      i0 = 0; i1=0; i2=0; i3=0; i4=0; i5=1; i6=0; i7=0;
      #1
      i0 = 0; i1=0; i2=0; i3=0; i4=0; i5=0; i6=1; i7=0;
      #1
      i0 = 0; i1=0; i2=0; i3=0; i4=0; i5=0; i6=0; i7=1;
      #1
   end
endmodule
