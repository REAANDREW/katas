typedef struct Node{
    void* value;
    struct Node *next;
    struct Node *previous;
} Node;

typedef struct Stack{
    struct Node *first;
} Stack;


Node*
createNode(void* item);

Stack*
createStack(void* item);

void
push(Stack *stack, void* data);

void*
pop(Stack *stack);
