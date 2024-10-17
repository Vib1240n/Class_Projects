/* ----------------------------------------------------------------- */
/*                  process_input                                    */
/* ----------------------------------------------------------------- */
#include "lab9_10.h"

void process_input(int argc, char **argv) {                       
    int returnValue;
    // Step 1: Call handle_redir to deal with operators:            
    //< , or  >, or both                                           
    Redirection(argc, argv);
    returnValue = execvp( argv[0], argv);

    //Step 2: perform system call execvp to execute command        
    //Hint: Please be sure to review execvp.c sample program       
    if (returnValue == -1) {                                        
       fprintf(stderr, "Error on the exec call\n");             
       _exit(EXIT_FAILURE);                                      
    }                                                            
}
/* ----------------------------------------------------------------- */