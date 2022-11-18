#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int numOfProcs;

struct process {
        int id;
        int timeNeeded;
        int priority;
        bool usedPriority;
        int slices;
        int waitTime;
        int turnAround;
       };

struct process rawInput[];

void fcfs() {
    struct process readyQ[numOfProcs];
    double totalTime = 0;
    double totalWait = 0;
    double totalTA = 0;
    float throughput;
    int i;

    for(i = 0; i < numOfProcs; i++) {
        readyQ[i] = rawInput[i];
    }
    printf("\nProcess list in FCFS order entered:\n");
    for(i = 0; i < numOfProcs; i++) {
        printf("%d %d %d\n", readyQ[i].id, readyQ[i].timeNeeded, readyQ[i].priority);
        readyQ[i].waitTime += totalTime;
        readyQ[i].turnAround += readyQ[i].waitTime + readyQ[i].timeNeeded;
        totalTime += readyQ[i].timeNeeded;
    }
    printf("End of List\n");

    for(i = 0; i < numOfProcs; i++) {
        printf("FCFS Wait of p%d = %d\n", readyQ[i].id, readyQ[i].waitTime);
        totalWait += readyQ[i].waitTime;
    }
    printf("Average Wait Time for %d procs = %0.1f\n", numOfProcs, (double)(totalWait/numOfProcs));

    for(i = 0; i < numOfProcs; i++) {
        printf("FCFS Turn-Around time for p%d = %d\n", readyQ[i].id, readyQ[i].turnAround);
        totalTA += readyQ[i].turnAround;
    }
    printf("Acerage Turn-Around for p%d procs = %0.1f\n", numOfProcs, (double)(totalTA/numOfProcs));

    printf("FCFS throughput for %d procs = %f proc/ms\n", numOfProcs, (double)(numOfProcs/totalTime));
    printf("<><> end FCFS Schedule <><>\n\n");
}

void hpf() {
    struct process readyQ[numOfProcs];
    int rIndex = 0;
    int uIndex;
    double totalTime = 0;
    double totalWait = 0;
    double totalTA = 0;
    float throughput;
    int currentP = 100;
    int lastUsedP = -1;
    struct process curHighProcs;
    int i;

    while (rIndex != numOfProcs) {
        for (i = 0; i < numOfProcs; i++) {
            if((rawInput[i].priority < currentP) && (rawInput[i].priority > lastUsedP) && (rawInput[i].usedPriority != true)) {
                currentP = rawInput[i].priority;
                curHighProcs = rawInput[i];
                uIndex = i;
            }
        }
        readyQ[rIndex] = curHighProcs;
        currentP = 100;
        lastUsedP = curHighProcs.priority;
        rawInput[uIndex].usedPriority;
        rIndex++;
    }
    printf("\nProcess list in HPF order:\n");
    for(i = 0; i < numOfProcs; i++) {
        printf("%d %d %d\n", readyQ[i].id, readyQ[i].timeNeeded, readyQ[i].priority);
        readyQ[i].waitTime += totalTime;
        readyQ[i].turnAround += readyQ[i].waitTime + readyQ[i].timeNeeded;
        totalTime += readyQ[i].timeNeeded;
    }
    printf("End of List.\n\n");

    for (i = 0; i < numOfProcs; i++) {
        printf("HPF wait of p%d = %d\n", readyQ[i].id, readyQ[i].waitTime);
        totalWait += readyQ[i].waitTime;
    }
    printf("Average Wait Time for %d procs = %0.3f\n", numOfProcs, (double)(totalWait/numOfProcs));

    for (i = 0; i < numOfProcs; i++) {
        printf("HPF Turn-Around time for p%d = %d\n", readyQ[i].id, readyQ[i].turnAround);
        totalTA += readyQ[i].turnAround;
    }
    printf("Average Turn-Around for %d procs = %0.1f\n", numOfProcs, (double)(totalTA/numOfProcs));
    printf("HPF throughput for %d procs = %f proc/ms\n", numOfProcs, (double)(numOfProcs/totalTime));
    printf("<><> End HPF Schedule <><>\n\n");
}

void rr(){
    struct process readyQ[numOfProcs];
    double totalTime = 0;
    double totalTimeLeft = 0;
    double compTime = 0;
    double avgTime;
    float throughput;
    int quantum = 1;
    int overhead = 1;
    double totalTA;
    bool complete = false;
    int i;

    for (i = 0; i < numOfProcs; i++) {
        readyQ[i] = rawInput[i];
    }

    printf("\nProcess list for RR in order entered:\n");
    for (i = 0; i < numOfProcs; i++) {
        printf("%d %d %d\n", readyQ[i].id, readyQ[i].timeNeeded, readyQ[i].priority);

    }
    printf("End of List.\n");

    int totalQuantum = 1;
    overhead = 0;
    while ((totalQuantum <= quantum) && (overhead <= quantum)) {
        for (i =0; i < numOfProcs; i++) {
            if (readyQ[i].timeNeeded == 0) {
                continue;
            } else {
                readyQ[i].waitTime += totalTime - (quantum * readyQ[i].slices);
                if (readyQ[i].timeNeeded - totalQuantum == 0 || readyQ[i].timeNeeded < totalQuantum) {
                    totalTime += totalQuantum;
                    readyQ[i].slices++;
                    readyQ[i].timeNeeded = 0;
                } else {
                    totalTime += totalQuantum;
                    readyQ[i].slices++;
                    readyQ[i].timeNeeded -= totalQuantum;
                }
                totalTime += overhead;
            }
        }
        for(i = 0; i < numOfProcs; i++) {
            totalTimeLeft += readyQ[i].timeNeeded;
        }
        printf("\nPreemptive RR schedule, quantum = %d overhead = %d\n", totalQuantum, overhead);
        for(i = 0; i < numOfProcs; i++) {
            readyQ[i].turnAround = readyQ[i].waitTime + rawInput[i].timeNeeded;
            printf("RR TA for finished p%d = %d, needed: %d ms, and %d time slices.\n", readyQ[i].id, readyQ[i].turnAround, rawInput[i].timeNeeded, readyQ[i].slices);
            totalTA += readyQ[i].turnAround;
            if (compTime < readyQ[i].turnAround) {
                compTime = readyQ[i].turnAround;
            }
        }
            printf("RR throughput, %d procs, with q: %d, o: %d, is %f p/ms, or %0.3f p/us\n", numOfProcs, totalQuantum, overhead, (double)(numOfProcs/compTime), (float)(1000*(numOfProcs/compTime)));
            printf("Average RR Turn-Around, %d procs, with q: %d, o: %d, is %0.1f\n", numOfProcs, totalQuantum, overhead, (double)(totalTA/numOfProcs));
        overhead++;
        if(overhead > totalQuantum){
            totalQuantum++;
            overhead = 0;
        }
    }
    printf("<><> End Preeptive RR Schedule <><>\n\n");
}

int main (int argc, char* argv[]){
    int a,b,c;

    if (argc != 1) {
        fprintf(stderr, "Error: Please enter [out_file name]");
        exit(-1);
    } else {
        printf("Enter triples: Process id, Time in ms, and Priority. Enter 'end' when done\n");
        printf("For example:\n");
        printf("1 12 0\n");
        printf("3 9 1\n");
        printf("2 99 9\n");
        printf("end\n");
        printf("process 1 needs 12 ms and has priority 0 (highest)\n");
        printf("process 3 needs 9 ms and has priority 1\n");
        printf("and so on...\n");
        while(scanf("%d %d %d", &a, &b, &c) == 3) {
            numOfProcs ++;
            rawInput[numOfProcs - 1].id = a;
            rawInput[numOfProcs - 1].timeNeeded = b;
            rawInput[numOfProcs - 1].priority = c;
            rawInput[numOfProcs - 1].usedPriority = false;
            rawInput[numOfProcs - 1].slices = 0;
            rawInput[numOfProcs - 1].waitTime = 0;
            rawInput[numOfProcs - 1].turnAround = 0;
        }
        fcfs();
        hpf();
        rr();
    }
}
