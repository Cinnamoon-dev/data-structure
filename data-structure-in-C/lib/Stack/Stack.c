#include "Stack.h"

void push(node** stack, int data) {
    node* new = create_node();
    
    if((*stack) == NULL) {
        new->data = data;
        new->next = NULL;

        (*stack) = new;
        return;
    }

    new->data = data;
    new->next = (*stack);
    (*stack) = new;
}

void push_array(node** stack, int* array, int size) {
    for(register int i = 0; i < size; i++) {
        push((*&stack), array[i]);
    }
}

void push_stack(node** stack, node* data) {
    node* aux = data;

    while(aux != NULL) {
        push(&stack, aux->data);
        aux = aux->next;
    }
}

int pop(node** stack) {
    if((*stack) == NULL) {
        return NULL;
    }

    if((*stack)->next == NULL) {
        int data = (*stack)->data;
        
        free((*stack));
        (*stack) = NULL;

        return data;
    }

    node* deleted_node = (*stack);
    int data = deleted_node->data;
    
    (*stack) = (*stack)->next;
    free(deleted_node);
    return data;
}

void print_stack(node* stack) {
    node* aux = stack;
    printf("[");
    printf("%d,", aux->data);

    aux = aux->next;

    while(aux != NULL) {
        if(aux->next == NULL) {
            printf(" %d", aux->data);
            aux = aux->next;
            
            continue;
        }

        printf(" %d,", aux->data);
        aux = aux->next;
    }

    printf("]\n");
}

int peak(node* stack) {
    return stack->data;
}

bool is_empty(node* stack) {
    return stack == NULL ? true : false;
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

int last(node* stack) {
    node* aux = stack;

    while(aux->next != NULL) {
        aux = aux->next;
    }

    return aux->data;
}

int get_value_by_index(node* stack, int index) {
    node* aux = stack;
    int counter = 0;

    while(counter != index && aux != NULL) {
        aux = aux->next;
        counter++;
    }

    if(aux == NULL) {
        return NULL;
    }

    return aux->data;
}