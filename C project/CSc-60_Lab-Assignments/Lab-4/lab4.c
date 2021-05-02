/*--------------------------------------------*/
/* Vibhore Sagar                                  */
/* Lab 4                                      */
/* Figure the area of a parabola using files  */

#include <stdio.h>
#include <stdlib.h>

#define IN_FILE_NAME "lab4.dat"
#define OUT_FILE_NAME "lab4.txt"

int main(void)
{
    double length, depth, area;
    FILE *infile;
    FILE *outfile;
    infile = fopen ("lab4.dat", "r");	
    if(infile == NULL)
    {
         printf("Error on opening the input file \n");       
         exit (EXIT_FAILURE);   // ( ) required since exit is a function
    } 

	outfile = fopen ("lab4.txt", "w");
    if(outfile == NULL)
    {
         printf("Error on opening the output file \n");
         exit (EXIT_FAILURE);  
    }
	
    /* Now that the files are open, we can use them */
    fprintf(outfile, "Vibhore Sagar,  Lab 4. \n\n");
    fprintf(outfile, "Data on Parabolas \n\n");
    fprintf(outfile, " Length      Depth        Area   \n");
    fprintf(outfile, "--------   ---------   --------- \n");
    
     while ((fscanf(infile, "%lf%lf", &length, &depth)) == 2)
     {
        area = (2*(length*depth))/3;
        fprintf(outfile, " %7.2f %10.2f %12.3f \n", length, depth, area);
        //fprintf(outfile, "\n\n");
     }    
     fclose(infile);
     fclose(outfile);
     return EXIT_SUCCESS;
}
/*---------------------------------------------------*/
