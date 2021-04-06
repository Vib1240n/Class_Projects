/*--------------*/
/* Vibhore Sagar */
/* Lab 3         */

#include <stdio.h>
#include <stdlib.h>

int main(void){
 int r, c, x[4][3];                                

for (r = 0; r < 4; r++)  {                        
     for (c = 0; c < 3; c++)      
         x[r][c] = r + c;

} 


return EXIT_SUCCESS;
}