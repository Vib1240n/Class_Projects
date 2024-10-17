#include <spede/stdio.h>

void toggle_case(char *str) {
    // Toggle the alphanumeric case for the passed-in string
}

int main(void) {
    char class_welcome[] = "Welcome to CPE/CSC 159 for Fall 2022!\n";

    printf(class_welcome);

    toggle_case(class_welcome);

    printf(class_welcome);

    toggle_case(class_welcome);

    printf(class_welcome);

    toggle_case(NULL);

    return 0;
}

