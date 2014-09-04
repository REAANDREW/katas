typedef struct Node{
    void* value;
    struct Node *next;
} Node;

typedef struct Queue{
    struct Node *first;
    struct Node *last;
} Queue;

Node*
createNode(void* data);

Queue*
createQueue(void* data);

void
enqueue(Queue *queue, void* item);

void*
dequeue ();
