#include <stdlib.h>
#include <stdio.h>

typedef struct _Node{
    int dado; 

    struct _Node* direita;
    struct _Node* esquerda;
} Node ;

void inserir_dado( Node** ptr_root_tree,  int dado )
{
    Node* node_temp = (Node*) calloc( 1 , sizeof(Node));
    node_temp->dado = dado ;

    if ( (*ptr_root_tree) == NULL){
        
        (*ptr_root_tree) = node_temp;
        return ;

    }

    Node* current_pointer = (*ptr_root_tree);
    Node* parent_pointer = NULL;

    while(1){
        // é responsável por sempre apontar para o nó superior
        parent_pointer = current_pointer; 

        if( dado < parent_pointer->dado )
        {
            current_pointer = current_pointer->esquerda; 
            // inserindo os menores na esquerda

            if( current_pointer == NULL)
            {
                parent_pointer->esquerda = node_temp;
                return ;
            }
            continue;
        }
        current_pointer = current_pointer->direita;
        // inserindo os maiores na direita

        if( current_pointer == NULL )
        {
            parent_pointer->direita = node_temp;
            return ;
        }
    }

    return ; 
}

void inOrderTransversal(Node* ptr_root_tree )
{
    if( ptr_root_tree ){
        inOrderTransversal(ptr_root_tree->esquerda);
        printf("[%d]",     ptr_root_tree->dado    );
        inOrderTransversal(ptr_root_tree->direita );
    }
}


int main() {
    Node* root_tree = NULL;
    int values_for_tree[14] ={34, 84, 15, 0, 2, 99, 79, 9, 88, 80, 18, 31, 39, 100};

    for (int i = 0; i < 14; i++) 
    {
        inserir_dado( &root_tree, values_for_tree[i]);
        printf("Inserted: %d\n", values_for_tree[i]);
    }
    
    printf("\n\nPrintingInOrderTheValues:\n\n");
    inOrderTransversal( root_tree );
    printf("\n");

    return 0;
}