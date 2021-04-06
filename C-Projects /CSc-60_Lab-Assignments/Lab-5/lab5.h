// Lab 5 header file
// This file should not have any code added to it.
// This file must be included in your function find_box_values.c

#include <stdio.h>
#include <stdlib.h>

#define IN_FILENAME  "lab5.dat"
#define OUT_FILENAME "lab5.txt"

/* File Pointers */
FILE * open_out_file(void);
FILE * open_in_file(void);

/* Function Prototypes */
void print_headers(FILE *data_out);
void find_box_values(FILE *data_out, FILE *data_in, double l, double h, double w, double*vol, double*s_area);	   
 
