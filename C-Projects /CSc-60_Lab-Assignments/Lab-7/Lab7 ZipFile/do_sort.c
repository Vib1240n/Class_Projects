/*--------------------------------------------------------*/
/* do_sort is a function to sort the drivers based on     */
/* their best times                                       */

#include "lab7.h"

void do_sort (driver_t driver_list[NRACERS])  
{
   int k, j, m; 
   driver_t hold;
 
   /* start the selection sort algorithm */
   for (k=0; k < NRACERS-1; k++)
   {
      /* exchange min with next array value */
      m = k;
      for (j = k+1; j < NRACERS; j++)
      {
	    if ( driver_list[j].d_best_time < driver_list[m].d_best_time )
	        m = j;
      }
      hold = driver_list[m];
      driver_list[m] = driver_list[k];
      driver_list[k] = hold;
   }
   return;
}

/*--------------------------------------------------------*/
