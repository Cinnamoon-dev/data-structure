#ifndef FUNC_H
#define FUNC_H

typedef struct{
    int dado;
    struct celula* prox;
}celula;

typedef struct{
    celula* head;
    celula* tail;
}fila;


fila* createFila();
int listData( fila* ptr );
fila* delete( fila* ptr );
int first_element(fila* ptr);
fila* insertData( fila* ptr, int dado );

#endif FUNC_H