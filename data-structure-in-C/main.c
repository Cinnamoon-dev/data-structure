#include "./lib/LinkedList/LinkedList.h"
#include "./lib/Stack/Stack.h"

int main() {
    node* stack = NULL;
    int a[3] = {7, 4, 3};

    push_array(&stack, a, 3);
    print_stack(stack);
    printf("%d\n", get_value_by_index(stack, 0));
    return 0;
}