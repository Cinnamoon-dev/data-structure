#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int data;
    struct node* next;
} node;

node* create_node() {
    node* new = (node*) malloc(sizeof(node));
    return new;
}

node* insert_node(node* list, int data) {
    node* new = create_node();
    node* aux = list;
    new->data = data;
    
    if(list == NULL) {
        list = new;
        new->next = NULL;

        return list;
    }

    while(aux->next != NULL) {
        aux = aux->next;
    }
    
    aux->next = new;
    new->next = NULL;

    return list;
}

void read_node(node* list) {
    node *aux = list;

    while(aux != NULL) {
        printf("%d\n", aux->data);
        aux = aux->next;
    }
    printf("\n");
}

node* delete_node(node* list) {
    if(list == NULL) {
        printf("You can't delete from an empty list!\n");
        return list;
    }

    node* aux = list;
    list = list->next;
    free(aux);

    return list;
}

int main() {
    node *list = NULL;

    list = insert_node(list, 1);
    list = insert_node(list, 2);
    list = insert_node(list, 3);
    list = insert_node(list, 4);
    list = insert_node(list, 5);
    read_node(list);

    list = delete_node(list);
    list = delete_node(list);
    list = delete_node(list);
    read_node(list);

    return 0;
}