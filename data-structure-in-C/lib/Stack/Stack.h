#ifndef STACK_H
#define STACK_H

#include "../LinkedList/LinkedList.h"

void push(node** stack, int data);

void push_array(node** stack, int* array, int size);

void push_stack(node** stack, node* data);

int pop(node** stack);

void print_stack(node* stack);

int peak(node* stack);

bool is_empty(node* stack);

int length(node* stack);

int last(node* stack);

int get_value_by_index(node* stack, int index);

#endif