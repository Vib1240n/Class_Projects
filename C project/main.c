#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    fork();
    fork();
    fork();
    fork();
    fprintf(stderr, "Hello\n");
    return 0;
}