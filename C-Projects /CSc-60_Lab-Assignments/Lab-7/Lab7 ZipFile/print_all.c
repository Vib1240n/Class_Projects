/*--------------------------------------------------------*/
/* This function will print everything out.               */

#include "lab7.h"

void print_all(FILE * out_file,
	       driver_t driver_list[NRACERS] ,
	       stats_t *race_stats ) 
{
	int d,t;

	fprintf(out_file, "\nYour Name.  Lab 7 output. \n");

	fprintf(out_file, "\nTrack Results");

	fprintf(out_file,"\n\nDrivers                  Try 1  "
		"     Try 2       Try 3      Best Time   Deviation");
	fprintf(out_file,  "\n--------------------   ---------"
		"   ---------   ---------   ----------   ---------\n");                          

	for (d = 0; d< NRACERS; d++)
	{
		fprintf(out_file, "%20s", driver_list[d].d_name);
		for (t = 0; t < TRIES; t++)
	      		fprintf(out_file, "   %8.3f ", driver_list[d].d_tries[t] );

		fprintf(out_file, "    %8.3f", driver_list[d].d_best_time );
		fprintf(out_file, "    %8.3f\n", driver_list[d].deviation);
	}

	fprintf(out_file, "\n\n The average of best times = %8.3f ", race_stats->average_of_best);
	fprintf(out_file, "\n\n The track fast time       = %8.3f ", race_stats->winning_time);
	fprintf(out_file, "\n\n The track slow time       = %8.3f ", race_stats->slowest_time);
	fprintf(out_file, "\n\n The median of best times  = %8.3f ", race_stats->median);
	fprintf(out_file, "\n\n");
	return;
}

/*--------------------------------------------------------*/
