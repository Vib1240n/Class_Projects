#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_INPUT 1000
char input[MAX_INPUT];

// List of all commands
char * cmds[] = {
       "cd",
       "exec",
       "exit",
       "gcc",
       "ls",
       "man",
       "more",
       "mv",
       "rm",
       "pwd",
       "sh",
       "touch",
       "which",
       "$path"
   };
 
//cmd temporarily holds the current command
char cmd[MAX_INPUT];
 
int main(int argc, char* argv[]) {
   //initialize variables i and index
   int i, index, cmdlen, currIndex = 0;
   char *token, *parsedStr[MAX_INPUT];
   //null input
   input[0] = 0;
   printf("VS cli 04/27/2022\n");
   printf("Legal Commands: ");
   for( i =0; cmds[i]; i++){
       printf("%s ", cmds[i]);
       cmdlen++;
   }
   //print out passed in commands
   printf("\n%d strings passed to argv[]\n", argc);
   for(i = 1; i<argc; i++){
       printf("next string is '%s'\n", argv[i]);
       strcat(input, argv[i]);
       strcat(input, " ");
       printf("new string is '%s'\n", input);
   }
   index = 0;
   //tokenize the commands
   token = strtok(input, ",;");
        while (token != NULL) {            
            parsedStr[index] = token;
            token = strtok(NULL, ",;");
            index++;
        }

    //system call commands while comparing them to legal commands
    for(i = 0; i < index; i++){
       while(currIndex < cmdlen) {
            if(strcmp(parsedStr[i], cmds[currIndex])){
                printf("cmd '%s' is one of the predefined.\n", parsedStr[i]);
                system(parsedStr[i]);
                break;
            }else{
                printf("ERROR: Not in Commands");
            }
        }
    }
   return 0;
}