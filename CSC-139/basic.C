#include <stdlib.h>
#include <stdio.h>

int main(void){

    printf("LS: %d", system("ls"));
    system("whoami");
    system("pwd");
    return EXIT_SUCCESS;
}