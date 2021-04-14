/*-----------------------------------------------------------*/
/* Lab 5.c  */

#include "lab7.h"

int main(void)
{
	struct driver_t driver_list[NRACERS];
	struct 
	stats_t race_stats = {0.0, 0.0, 0.0, 0.0};  
	
   	FILE * out_file;   /* file pointer for the output file    */
			
	/* Start the action. */

	out_file = open_out_file ();
	get_data(IN_FILENAME, driver_list);
	get_stats(driver_list, &race_stats);
	do_sort(driver_list);
	get_median(driver_list, &race_stats);
	print_all(out_file, driver_list, &race_stats);

	return EXIT_SUCCESS;
}

/*----------------------------------------------------------*/
