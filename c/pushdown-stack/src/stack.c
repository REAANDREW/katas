#include <stdlib.h>
#include "stack.h"

Node*
createNode(void* item){
    Node *data = (Node *) malloc(sizeof(Node));
    data->value = item;
    return data;
}

Stack*
createStack(void* item){
    Stack *stack = (Stack *) malloc(sizeof(Stack));
    Node *first = createNode(item);
    stack->first = first;
    return stack;
}

void
push(Stack *stack, void* data){
    Node *oldFirst = stack->first;
    Node *first = createNode(data);
    first->next = oldFirst;
    stack->first = first;
}

void*
pop(Stack *stack){
    Node *first = stack->first;
    stack->first = first->next;
    void* value = first->value;
    free(first);
    return value;
}
