#include <stdio.h>
#include <stdlib.h>

typedef struct _celula {
    int dado;
    struct _celula* prox;
} celula;

celula* createCelula( int dado, celula* prox )
{
    celula* ptr = malloc( sizeof( celula ) );
    ptr->dado = dado;
    ptr->prox = prox;

    return ptr;
}

void insertData( celula** fila_celulas, int dado)
{
    celula* aux = *fila_celulas;

    while ( aux->prox != NULL )
    {
        aux = aux->prox;
    }

    celula* new_celula = createCelula( dado, NULL );
    aux->prox = new_celula;

    return ;
}

void listData( celula* fila_celulas )
{
    celula* aux = fila_celulas;

    while( aux != NULL )
    {
        printf(">>%d\n", aux->dado);
        aux = aux->prox;
    }

    return ;
}

int deleteData(celula** fila_pointer)
{
    int aux = (*fila_pointer)->dado;
    celula* first_celula = (*fila_pointer);

    (*fila_pointer) = (*fila_pointer)->prox;

    free(first_celula);

    return aux;
}

int peekElement( celula* fila_pointer )
{
    // return the first element of my data structure 
    return fila_pointer->dado;
}

int isEmpty( celula* fila_pointer )
{
    return !(fila_pointer != NULL);
}

int lengthFila( celula* fila_pointer )
{
    if (fila_pointer == NULL){
        return -1;
    }

    int counter = 0;

    while( fila_pointer != NULL){
        counter++;
        fila_pointer = fila_pointer->prox;
    }

    return counter;
}

int lastElement( celula* fila_pointer ){
    
    if(fila_pointer == NULL){
        return -1;
    }

    celula* aux_pointer = fila_pointer;
    
    while( aux_pointer->prox != NULL ){
        aux_pointer = aux_pointer->prox;
    }

    int last_element = aux_pointer->dado;

    return last_element;
}

int getValueByIndex( celula* fila_pointer, int index ){

    if( (fila_pointer == NULL) || index > lengthFila(fila_pointer) ){
        return -1;
    }

    int counter = 0;
    celula* aux_pointer = fila_pointer;

    while( aux_pointer != NULL ){

        if( index == counter ){
            return aux_pointer->dado;
        }

        counter += 1;
        aux_pointer = aux_pointer->prox;
    }
    return -1;
}

int getIndexByValue( celula* fila_pointer, int dado ){

    if( fila_pointer == NULL ){
        return -1;
    }

    int counter = 0;
    celula* aux_pointer = fila_pointer;

    while( aux_pointer != NULL ){
        if( aux_pointer->dado == dado ){
            return counter;
        }
        aux_pointer = aux_pointer->prox;
    }
    return -1;
}

void getAllIndexByValue( celula* fila_pointer, int** result,int dado ){
    
    if( fila_pointer == NULL ){
        return ;
    }

    int length_array = 1;
    int index_array = 0;
    (*result) = malloc( length_array * sizeof(int) );

    int counter = 0;
    celula* aux_pointer = fila_pointer;

    while( aux_pointer != NULL )
    {    
        if( aux_pointer->dado == dado )
        {
            length_array++;
            (*result) = realloc( (*result) , length_array * sizeof(int));
            *( (*result) + index_array ) = counter;
            index_array++;
        }
        counter += 1;
        aux_pointer = aux_pointer->prox;
    }
}

int main()
{
    celula* f_ptr = createCelula(100, NULL);
    int* indexs = NULL;

    insertData( &f_ptr, 120 );
    insertData( &f_ptr, 140 );
    insertData( &f_ptr, 160 );
    insertData( &f_ptr, 140 );

    listData(f_ptr);
    printf(">>%d, length of my queue\n", lengthFila(f_ptr));
    printf(">>%d, last element of my queue\n", lastElement(f_ptr));
    printf(">>%d, get element by index \n", getValueByIndex(f_ptr, 2));

    getAllIndexByValue(f_ptr, &indexs, 140);

    for(int i = 0; i < 2 ; ++i)
    {
        printf("data in index %d, >> %d\n", i, *(indexs + i));
    }

    return 0;
}