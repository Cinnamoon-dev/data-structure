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

    return;
}

void push_array(node** stack, int* data, int size) {
    for (register int i = 0; i < size; i++) {
        push(&stack, data[i]);
    }
}

void push_node(node** stack, node* data) {
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

    node* aux = (*stack);
    int value = (*stack)->data;
    
    (*stack) = (*stack)->next;
    free(aux);

    return value;
}

void print(node* stack) {
    node* aux = stack;

    while(aux != NULL) {
        printf("%d\n", aux->data);
        aux = aux->next;
    }
    printf("\n");
}

int peak(node* stack) {
    return stack->data;
}

bool is_empty(node *stack) {
    if(stack == NULL) {
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

int last(node* stack) {
    return peak(stack);
}

int get_value_by_index(node* stack, int index) {
    node* new_stack = NULL;
    int aux, value, counter = 0;
    bool found = false;

    while(stack != NULL) {
        push(&new_stack, pop(&stack));
    }

    while(new_stack != NULL) {
        aux = pop(&new_stack);
        push(&stack, aux);        
        
        if(counter == index) {
            value = aux;
            found = true;
        }
        
        counter++;
    }

    if(found == false) {
        return -1;
    }

    return value;
}

int get_index_by_value(node* stack, int value) {
    node* new_stack = NULL;
    int aux, index, counter = 0;
    bool found = false;

    while(stack != NULL) {
        push(&new_stack, pop(&stack));
    }

    while(new_stack != NULL) {
        aux = pop(&new_stack);
        push(&stack, aux);

        if(aux == value) {
            found = true;
            index = counter;
        }
        counter++;
    }

    if(found == false) {
        return -1;
    }

    return index;
}

int* get_all_indexes_by_value(node* stack, int value) {
    node* new_stack = NULL;
    int* indexes = NULL;
    int aux, counter = 0, array_counter = 0;

    while(stack != NULL) {
        push(&new_stack, pop(&stack));
    }

    while(new_stack != NULL) {
        aux = pop(&new_stack);

        if(aux == value) {
            indexes = malloc(sizeof(int));
            *(indexes + array_counter) = aux;
            array_counter++;
        }

        counter++;
    }

    return indexes;
}

int main() {
    node *stack = NULL;

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);
    push(&stack, 4);
    push(&stack, 5);
    print(stack);
    pop(&stack);
    printf("valor = %d\n", get_value_by_index(stack, 5));
    print(stack);
    return 0;
}