/*-----------------------------------------------------------*/
/* This function will open and read data into an array.      */

#include "lab7.h"

void get_data (char *filename,                    /* input   */ 
	       driver_t driver_list[NRACERS])     /* output  */
{
	int d;
	FILE *in_file;

	/* Open the data file and read in the array */
	in_file = fopen(filename, "r");
	if (in_file == NULL)
	{
		printf("Error on fopen of %s \n", filename);
		exit(EXIT_FAILURE);
	}

	/* Use an "d" for Driver. */
	for(d = 0; d < NRACERS; d++)
	{
	   fscanf(in_file, "%20c%lf%lf%lf\n", 
		      &(driver_list[d].d_name),
		      &(driver_list[d].d_tries[0]),
	          &(driver_list[d].d_tries[1]),
	          &(driver_list[d].d_tries[2]) ); 
	          
	   driver_list[d].d_name[20] = '\0';
	}

	fclose(in_file);
	return;
}

/*----------------------------------------------------------------*/
