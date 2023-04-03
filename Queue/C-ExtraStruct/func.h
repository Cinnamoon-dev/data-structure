#ifndef FUNC_H
#define FUNC_H

typedef struct{
    int dado;
    struct celula* prox;
}celula;

typedef struct{
    celula* inicio;
    celula* fim;
}fila;


fila* createFila();
int listData( fila* ptr );
int popWithClassLinkedList( fila** ptr );
int first_element(fila* ptr );
fila* pushWithClassLinkedList( fila* ptr, int dado );

#endif