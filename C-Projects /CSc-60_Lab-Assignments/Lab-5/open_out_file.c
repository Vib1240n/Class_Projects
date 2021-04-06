// Ruthann Biel
//
#include "lab5.h"

FILE * open_out_file (void)
{
    FILE * data_out;

    data_out = fopen(OUT_FILENAME, "w");
    if (data_out == NULL)
    {
        printf("Error on fopen of %s \n", OUT_FILENAME);
        exit(EXIT_FAILURE);
    }
    return data_out;
}
