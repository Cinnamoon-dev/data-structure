#include <stdlib.h>
#include <stdio.h>
#include "./func.h"


int main(){
    fila* fila = createFila();    

    fila = pushWithClassLinkedList(fila, 100);
    fila = pushWithClassLinkedList(fila, 120);
    fila = pushWithClassLinkedList(fila, 140);
    fila = pushWithClassLinkedList(fila, 160);

    listData(fila);
    printf("first element -->%d\n", first_element(fila));

    printf("foi deletado >>%d\n", popWithClassLinkedList(&fila)); // FiFo

    listData(fila);

}