#include <stdlib.h>
#include <stdio.h>
#include "func.h"


fila* pushWithClassLinkedList( fila* ptr, int dado )
{
    celula* aux = malloc(sizeof(celula));
    aux->dado = dado;
    aux->prox = NULL;

    if( ptr->fim != NULL )
    {
        ptr->fim->prox = aux;
    }

    ptr->fim = aux;

    if( ptr->inicio == NULL )
    {
        ptr->inicio = aux;
    }

    return ptr;
}

fila* createFila()
{
    fila* ptr = malloc(sizeof(fila));
    
    ptr->inicio = NULL;
    ptr->fim = NULL;
    
    return ptr;
}

int listData( fila* ptr )
{
    celula* aux = ptr->inicio;

    while( aux != NULL  )
    {
        printf("%d\n", aux->dado);
        aux = aux->prox;
    }

    return 0;
}

int first_element(fila* ptr)
{
    return ptr->inicio->dado;
}

int popWithClassLinkedList( fila** ptr )
{
    fila* new_fila = createFila();
    int aux = (*ptr)->inicio->dado;

    new_fila->inicio = (*ptr)->inicio->prox;
    new_fila->fim = (*ptr)->fim;

    free((*ptr)->inicio);

    (*ptr) = new_fila;

    return aux;
}

