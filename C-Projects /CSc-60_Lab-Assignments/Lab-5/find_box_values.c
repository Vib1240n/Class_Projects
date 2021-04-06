//Vibhore Sagar
#include "lab5.h"

void find_box_values(FILE *data_out, FILE *data_in, double l, double h, double w, double*vol, double*s_area){
    
    while ((fscanf(data_in, "%lf%lf%lf", &l, &h, &w)) == 3){
        *vol = l*h*w;
        *s_area = 2 * (l*w  + h*w  + h*l);
        fprintf(data_out, " %-.2f  %8.2f %7.2f %9.2f %11.2f \n", l, h, w, *vol, *s_area );
    }
    fprintf(data_out, "\n\n");
}	 