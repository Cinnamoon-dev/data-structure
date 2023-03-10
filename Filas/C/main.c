#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int dado; // void *dado;
    struct celula* prox;

}celula;

celula* createCelula( int dado, celula* prox )
{
    celula* ptr = malloc(sizeof(celula));
    ptr->dado = dado;
    ptr->prox = prox;

    return ptr;
}

celula* insertData( celula* fila_celulas, int dado)
{
    celula* aux = fila_celulas;

    while ( aux->prox != NULL )
    {
        aux = aux->prox;
    }

    celula* new_celula = createCelula(dado, NULL);
    aux->prox = new_celula;


    return fila_celulas;
}

void listData( celula* fila_pointer )
{
    celula* aux = fila_pointer;

    while( aux != NULL )
    {
        printf(">>%d\n", aux->dado);
        aux = aux->prox;
    }

    return;
}

int delete(celula** fila_pointer)
{
    int aux = (*fila_pointer)->dado;
    celula* first_celula = (*fila_pointer);

    (*fila_pointer) = (*fila_pointer)->prox;

    free(first_celula);

    return aux;
}

int main()
{
    // create a new celula
    celula* f_ptr = createCelula(100, NULL);

    f_ptr = insertData(f_ptr, 120);
    f_ptr = insertData(f_ptr, 140);
    f_ptr = insertData(f_ptr, 160);

    listData(f_ptr);

    printf(">>%d, deleted\n", delete(&f_ptr));
    printf(">>%d, deleted\n", delete(&f_ptr));

    listData(f_ptr);

    return 0;
}