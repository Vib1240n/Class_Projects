# Vibhore Sagar, Lab5

lab5: lab5.o open_out_file.o open_in_file.o print_headers.o find_box_values.o
	gcc lab5.o open_out_file.o open_in_file.o print_headers.o find_box_values.o -o lab5 -lm

open_out_file.o: open_out_file.c lab5.h
	gcc -c open_out_file.c -lm

open_in_file.o: open_in_file.c lab5.h
	gcc -c open_in_file.c -lm

print_headers.o: print_headers.c lab5.h
	gcc -c print_headers.c -lm

find_box_values.o: find_box_values.c lab5.h
	gcc -c find_box_values.c