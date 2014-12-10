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
    int pId = uf_find(un,p);
    int qId = uf_find(un,q);

    if(pId == qId){
        return;
    }

    int length = sizeof(un->i) / sizeof(int);
    int index;

    for(index = 0; index < length; index++){
        if (un->i[index] == pId){
            un->i[index] = qId;
        }
    }

    un->count--;
    
}

int uf_find(Union *un, int p){
    printf("index required = %d\n", p);
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
