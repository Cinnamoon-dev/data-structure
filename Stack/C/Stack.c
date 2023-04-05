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

void array_push(node** stack, int* data, int size) {
    for (register int i = 0; i < size; i++) {
        push(&stack, data[i]);
    }
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
    node* aux = stack;

    while(aux->next != NULL) {
        aux = aux->next;
    }

    return aux->data;
}

int get_value_by_index(node* stack, int index) {
    node* new_stack = NULL;
    int aux, value, counter = 0;
    bool condition = true;

    while(stack != NULL) {
        push(&new_stack, pop(stack));
    }

    while(new_stack != NULL) {
        if(condition) {
            aux = pop(new_stack);
        }
        
        if(counter == index) {

        }
    }
}

int main() {
    node *stack = NULL;

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);
    push(&stack, 4);
    push(&stack, 5);
    print(stack);
    printf("%d\n", last(stack));
    return 0;
}