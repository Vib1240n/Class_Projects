#MakeFile
#Vibhor Sagar
lab10: lab10.o ParseLine.o ProcessInput.o Redirection.o RunExternalCommand.o 
	gcc lab10.o ParseLine.o ProcessInput.o Redirection.o RunExternalCommand.o -o lab10 -Wall
lab10.o: lab10.c lab9_10.h
	gcc -c lab10.c lab9_10.h -Wall
ParseLine.o: ParseLine.c lab9_10.h
	gcc -c ParseLine.c lab9_10.h -Wall
ProcessInput.o: ProcessInput.c lab9_10.h
	gcc -c ProcessInput.c lab9_10.h -Wall
Redirection.o: Redirection.c lab9_10.h
	gcc -c Redirection.c lab9_10.h  -Wall
RunExternalCommand.o: RunExternalCommand.c lab9_10.h
	gcc -c RunExternalCommand.c lab9_10.h  -Wall
