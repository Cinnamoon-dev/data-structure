#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int data;
    struct node* left;
    struct node* right;
} node;

node* insert_node(node *root, int data) {
    node *new = (node*) malloc(sizeof(node));

    new->data = data;
    new->left = NULL;
    new->right = NULL;

    if(root == NULL) {
        root = new;
        return root;
    }

    node* current = root;
    node* parent = NULL;

    while(1) {
        parent = current;

        if(data < parent->data) {
            current = current->left;

            if(current == NULL) {
                parent->left = new;
                return root;
            }
        }
        else {
            current = current->right;

            if(current == NULL) {
                parent->right = new;
                return root;
            }
        }
    }

    while(1) {
        parent = current;

        if(data < parent->data) {
            current = current->left;

            if(current == NULL) {
                parent->left = new;
                return root;
            }
            continue;
        }

        else if(data >= parent->data) {
            current = current->right;

            if(current == NULL) {
                parent->right = new;
                return root;
            }
        }
    }
    
    return root;
}

void inorder_transversal(node* root) {
    if(root) {
        inorder_transversal(root->left);
        printf("%d", root->data);
        inorder_transversal(root->right);
    }
}

node* search(node* root, int data) {
    node* current = root;
    printf("Visiting elements: ");

    while(current) {
        printf("%d ", current->data);

        if(data < current->data) {
            current = current->left;
        }
        else if(data > current->data) {
            current = current->right;
        }
        else {
            return current;
        }
    }
}

int main() {
    int i;
    int array[14] = 
        {34, 84, 15, 0, 2, 99, 79, 9,
         88, 80, 18, 31, 39, 100, 101};
    node* root = NULL;

    for (int i = 0; i < 13; i++) {
        root = insert(root, array[i]);
        printf("Inserted: %d\n", array[i]);
    }

    node* temp = search(root, 88);
    if(temp) {
        printf("[%d] Found\n", temp->data);
    }
    else {
        printf("[%d] Not found!\n", i);
    }

    return 0;
}