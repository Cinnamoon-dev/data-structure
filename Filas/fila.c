#include <stdlib.h>
#include <stdio.h>
#include "func.h"


int main(){
    fila* fila = createFila();    

    // insert a data in my fila
    fila = insertData(fila, 100);
    fila = insertData(fila, 120);
    fila = insertData(fila, 140);
    fila = insertData(fila, 160);

    listData(fila);
    printf("first element -->%d\n", first_element(fila));

    fila = delete(fila); // FiFo

    listData(fila);


}