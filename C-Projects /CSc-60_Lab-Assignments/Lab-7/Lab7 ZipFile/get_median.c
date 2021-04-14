#include "lab7.h"

void get_median(driver_t driver_list[NRACERS], stats_t *race_stats ){
    race_stats->median = 0;
    int mid = NRACERS /2 ;
    if(NRACERS % 2 != 0){
        race_stats->median = driver_list[mid].d_best_time;
    }else {
        double avg =(driver_list[mid].d_best_time + driver_list[mid+1].d_best_time) /2;
        race_stats->median = avg;
    }
}