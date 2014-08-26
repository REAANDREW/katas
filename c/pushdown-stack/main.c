#include <stdio.h>
#include "stack.h"

int
main(){
    Stack *stack = createStack("Some data for the top of the stack");
    push(stack, "Some more data");
    printf("%s\n", stack->first->value);
    printf("%s\n", stack->first->next->value);
    void* data = pop(stack);
    printf("%s\n", data);
    return 0;
}
