#Vibhore Sagar, Lab7

Lab7: lab7.o do_sort.o get_data.o get_median.o get_stats.o open_out_file.o print_all.o
	gcc lab7.o do_sort.o get_data.o get_median.o get_stats.o open_out_file.o print_all.o -o Lab7 

lab7.o: lab7.c lab7.h
	gcc -c lab7.c

do_sort.o: do_sort.c lab7.h
	gcc -c do_sort.c 

get_data.o: get_data.c lab7.c
	gcc -c get_data.c 

get_median.o: get_median.c lab7.h
	gcc -c get_median.c 

get_stats.o: get_stats.c lab7.h
	gcc -c get_stats.c  

open_out_file.o: open_out_file.c lab7.h
	gcc -c open_out_file.c

print_all.o: print_all.c lab7.h
	gcc -c print_all.c