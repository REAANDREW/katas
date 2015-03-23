#include <stdio.h>
#include "queue.h"

int
main(){
    Queue *queue = createQueue("first item");
    enqueue(queue, "second item");
    printf("Fifo example finished.\n");
}
