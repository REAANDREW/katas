#include <stdlib.h>
#include "queue.h"

Node* createNode(void* data){
    Node *item = (Node *) malloc(sizeof(Node));
    item->value = data;
    return item;
}

Queue* createQueue(void* data){
    Queue *queue = (Queue *) malloc(sizeof(Queue));
    Node *firstNode = createNode(data);
    queue->first = firstNode;
    queue->last = firstNode;
    return queue;
}

void
enqueue(Queue *queue, void* item){
    Node *oldLast = queue->last;
    Node *last = createNode(item);
    oldLast->next=last;
    queue->last = last;
}

void*
dequeue (Queue *queue){
    
}
