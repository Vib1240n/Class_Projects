#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

// execlp("/bin/ls","ls",NULL);

int main(){
    pid_t pid;
    pid = fork();
    if (pid < 0){
        return 1;
    }
    else if (pid == 0){
        execlp("/bin/ls", "ls", NULL);
    }
    else{
        wait(NULL);
        printf("Child Complete");
    }
    return 0;
}
