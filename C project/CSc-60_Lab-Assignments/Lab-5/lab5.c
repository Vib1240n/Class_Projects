/*-------------------------------------------------------*/
/* Ruthann Biel.                                         */
/* LAB 5, function that "returns" more than one value    */
/* Find the volume and the surface area of a rectangular */
/* box                                                   */


#include "lab5.h"

int main(void)
{
    double l, w, h;		/* measures of the box */
    double vol;  		/* volume of the box */	
    double s_area;		/* surface area of the box */

    FILE * data_in;      /* input file pointer */
    FILE * data_out;     /* output file pointer */

    
    data_out = open_out_file();

    data_in = open_in_file();


    print_headers(data_out);

    find_box_values(data_out, data_in, l, h, w, &vol, &s_area);

    fclose(data_in);
    fclose(data_out);
    return EXIT_SUCCESS;
}
/*-----------------------------------------------------------*/
