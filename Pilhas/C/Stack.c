#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int data;
    struct node* next;
} node;

node* create_node() {
    node* new = (node*) malloc(sizeof(node));
    return new;
}

void push(node** list, int data) {
    node* new = create_node();

    if((*list) == NULL) {
        new->data = data;
        new->next = NULL;

        (*list) = new;
        return;
    }

    new->data = data;
    new->next = list;
    list = new;

    return;
}

int pop(node** list) {
    if((*list) == NULL) {
        return NULL;
    }

    node* aux = (*list);
    int value = (*list)->data;
    
    (*list) = (*list)->next;
    free(aux);

    return value;
}

void print(node* list) {
    node* aux = list;

    while(aux != NULL) {
        printf("%d\n", aux->data);
        aux = aux->next;
    }
    printf("\n");
}

void array_push(node** list, int* data, int size) {
    for (register int i = 0; i < size; i++) {
        push(&list, data[i]);
    }
}

int peak(node* list) {
    return list->data;
}

bool is_empty(node *list) {
    if(list == NULL) {
        return true;
    }
    return false;
}

int length(node* stack) {
    node* aux = stack;
    int counter = 0;

    while(aux != NULL) {
        counter++;
        aux = aux->next;
    }

    return counter;
}

int main() {
    node *stack = NULL;

    push(&stack, 1);
    // list = insert_node(list, 2);
    // list = insert_node(list, 3);
    // list = insert_node(list, 4);
    // list = insert_node(list, 5);
    print(stack);

    // list = delete_node(list);
    // list = delete_node(list);
    // list = delete_node(list);
    // print(list);

    return 0;
}