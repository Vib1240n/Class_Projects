#include "lab7.h"

void get_stats(driver_t driver_list[NRACERS], stats_t *race_stats ){
    race_stats->average_of_best=0;
    race_stats->slowest_time = driver_list[0].d_tries[0];
    race_stats->winning_time = driver_list[0].d_tries[0];

    for(int i =0; i <NRACERS; i++){
        driver_list[i].deviation =0;
        driver_list[i].d_best_time = driver_list[i].d_tries[0];
        for(int j = 0; j < TRIES; j++){
            if(driver_list[i].d_tries[j] < driver_list[i].d_best_time){
                driver_list[i].d_best_time = driver_list[i].d_tries[j];
            }else{
                driver_list[i].d_best_time = driver_list[j].d_best_time;
            }

            if(driver_list[i].d_tries[j] > race_stats->slowest_time){
                race_stats->slowest_time = driver_list[i].d_tries[j];
            }

            if(driver_list[i].d_tries[j] > race_stats->slowest_time){
                race_stats->winning_time = driver_list[i].d_tries[j];
            }
        }
        race_stats->average_of_best += driver_list[i].d_best_time;
    }
    race_stats->average_of_best/=NRACERS;
    for(int i=0; i<NRACERS; i++){
        driver_list[i].deviation= race_stats->winning_time - driver_list[i].d_best_time;
    }
    return;
}