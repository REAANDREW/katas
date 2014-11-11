#include "uf.h"

Union uf(int n){
    int *i;
    i = malloc(n * sizeof(int)); 
    int index = 0;
    for(index = 0;index < n; index++){
        i[index] = index;   
    };
    Union value = {
        .count = n,
        .i = i
    };
    return value;
}

void uf_createUnion(Union *un, int p, int q){
    int pId = uf_find(p);
    int qId = uf_find(q);
}

int uf_find(Union *un, int p){
    printf("index required = %d", p);
    return un->i[p];
}

bool uf_connected(Union *un, int p, int q){
    return false;
}

int uf_count(Union *un){
    return un->count;
}

void uf_free(Union *un){
    free(un->i);
}
