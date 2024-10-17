/**
 * CPE/CSC 159 Operating System Pragmatics
 * California State University, Sacramento
 * Fall 2022
 *
 * C Refresher Test Program
 */

#include <spede/stdlib.h>   // for abort()
#include <spede/stdio.h>    // for printf()

#include "bit_util.h"
#include "queue.h"
#include "ringbuf.h"


int main(void) {
    queue_t my_queue;

    ringbuf_t my_buf;

    queue_in(&my_queue, 1);
    queue_in(&my_queue, 5);
    queue_in(&my_queue, 9);
    queue_in(&my_queue, 2);
    queue_in(&my_queue, 0);
    queue_in(&my_queue, 2);
    queue_in(&my_queue, 2);

    while (!queue_is_empty(&my_queue)) {
        int value;
        if (queue_out(&my_queue, &value) != 0) {
            printf("Error queueing out!\n");
            abort();
        }

        printf("%d ", value);
    }
    printf("\n\n");

    for (int i = 0; i < QUEUE_SIZE; i++) {
        if (queue_is_full(&my_queue)) {
            printf("Queue is full prematurely!\n");
            abort();
        }

        queue_in(&my_queue, i);
    }

    if (!queue_is_full(&my_queue)) {
        printf("Queue should be full!\n");
        abort();
    }

    int buf_size = 0;
    while (!ringbuf_is_full(&my_buf)) {
        ringbuf_write(&my_buf, 'A');
        buf_size++;
    }

    char my_char;
    while (!ringbuf_is_empty(&my_buf)) {
        ringbuf_read(&my_buf, &my_char);
        buf_size--;
    }

    if (buf_size != 0) {
        printf("Buffer should have been empty!\n");
        abort();
    }

    int value = 0;

    value = bit_set(value, 3);

    if (!bit_test(value, 3)) {
        printf("Bit 3 should be set!\n");
        abort();
    }

    if (bit_test(value, 4)) {
        printf("Bit 4 should not be set!\n");
        abort();
    }

    if (bit_test(value, 2)) {
        printf("Bit 2 should not be set!\n");
        abort();
    }

    value = bit_toggle(value, 3);
    if (bit_test(value, 3)) {
        printf("Bit 3 should not be set!\n");
        abort();
    }

    if (value != 0) {
        printf("Value should be 0\n");
        abort();
    }

    value = bit_toggle(value, 4);
    value = bit_toggle(value, 7);

    if (bit_count(value) != 2) {
        printf("Should only have two bits set!\n");
        abort();
    }

    return 0;
}

