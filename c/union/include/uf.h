#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Union {
    int count;
    int *i; 
} Union;

Union uf(int n);
void uf_createUnion(Union *un, int p, int q);
int uf_find(Union *un, int p);
bool uf_connected(Union *un, int p, int q);
int uf_count(Union *un);
void uf_free(Union *un);
