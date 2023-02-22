#include <stdlib.h>
#include <stdio.h>
#include "func.h"

fila* insertData( fila* ptr, int dado )
{
    celula* aux = malloc(sizeof(celula));
    aux->dado = dado;
    aux->prox = NULL;

    if( ptr->tail != NULL )
    {
        ptr->tail->prox = aux;
    }

    ptr->tail = aux;

    if( ptr->head == NULL )
    {
        ptr->head = aux;
    }

    return ptr;
}

fila* createFila()
{
    fila* ptr = malloc(sizeof(fila));
    
    ptr->head = NULL;
    ptr->tail = NULL;
    
    return ptr;
}

int listData( fila* ptr )
{
    celula* aux = ptr->head;

    while( aux != NULL  )
    {
        printf("%d\n", aux->dado);
        aux = aux->prox;
    }

    return 0;
}

int first_element(fila* ptr)
{
    return ptr->head->dado;
}

fila* delete( fila* ptr )
{
    fila* new_fila = createFila();

    new_fila->head = ptr->head->prox;
    new_fila->tail = ptr->tail;

    free(ptr->head);

    return new_fila;
}