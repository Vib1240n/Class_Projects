#include "lab9_10.h"

void Redirection(int argc, char *argv[]){
    int in = 0, out = 0, fd, i;
    for (i = 0; i < argc; i++){
        if(strcmp(">", argv[i]) == 0){
            if( out != 0){
                fprintf(stderr, "Error. Cannot output to more than one file \n");
                _exit(EXIT_FAILURE);
            }else if(i==0){
                fprintf(stderr, "No Command Entered \n");
                _exit(EXIT_FAILURE);
            }
            out = i;
        }else if(strcmp(argv[i], "<") ==0){
            if(in != 0){
                fprintf(stderr, "Error. Cannot input from more than one file \n");
            _exit(EXIT_FAILURE);
            }else if(i ==0){
                fprintf(stderr, "Error. No Command Entered \n");
            _exit(EXIT_FAILURE);
            }
            in = i;
        }
    }
    if (out !=0){
        if(argv[out+1] == NULL){
            fprintf(stderr, "Error. There is no file \n");
            _exit(EXIT_FAILURE);
        }
        fd = open(argv[out+1], O_RDWR | O_CREAT | O_TRUNC, S_IROTH | S_IWOTH);
        if(fd == -1){
            perror("Error Opening File");
        }
        dup2(fd, 1);
        close(fd);
        argv[out] = NULL;
    }
    if(in != 0 ){
        if(argv[in+1] == NULL){
            fprintf(stderr, "Error. There is no file \n");
            _exit(EXIT_FAILURE);
        }
        fd = open(argv[in+1], O_RDONLY);
        if(fd == -1){
            perror("Error Reading File");
            _exit(EXIT_FAILURE);
        }
        dup2(fd, 0);
        close(fd);
        argv[in] = NULL;
    }

}