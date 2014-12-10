#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "uf.h"

#define LINE_MAX 50

int main(int argc, char *argv[]){
    Union un;
    bool started = false;
    char line[LINE_MAX];
    char *p, *q;
    int number = 0;

    printf("about to process");
    while(fgets(line, LINE_MAX, stdin) != NULL){
        if(!started){
            number = atoi(line); 
            un = uf(number);
            started = true;
        }else{
            p = strtok( line, " " );
            q = strtok( NULL, " " );
            uf_createUnion(&un, atoi(p), atoi(q));
        }
    }

    int c = uf_find(&un, 2);
    printf("Complete %d", c);
    uf_free(&un);
}
