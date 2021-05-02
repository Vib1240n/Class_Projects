// Ruthann Biel
//
#include "lab5.h"

FILE *open_in_file (void)
{
    FILE *data_in;

    data_in = fopen(IN_FILENAME, "r");
    if (data_in == NULL)
    {
        printf("Error on fopen of %s \n", IN_FILENAME);
        exit(EXIT_FAILURE);
    }
    return data_in;
}
