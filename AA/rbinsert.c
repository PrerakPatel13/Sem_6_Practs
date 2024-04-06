#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    char color;
    struct Node *left, *right, *parent;
};

struct Node *createNode(int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->color = 'R';
    newNode->left = newNode->right = newNode->parent = NULL;
    return newNode;
}

void leftRotate(struct Node **root, struct Node *x) {
    struct Node *y = x->right;
    x->right = y->left;
    if (y->left != NULL)
        y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL)
        *root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;
    y->left = x;
    x->parent = y;
}

void rightRotate(struct Node **root, struct Node *y) {
    struct Node *x = y->left;
    y->left = x->right;
    if (x->right != NULL)
        x->right->parent = y;
    x->parent = y->parent;
    if (y->parent == NULL)
        *root = x;
    else if (y == y->parent->right)
        y->parent->right = x;
    else
        y->parent->left = x;
    x->right = y;
    y->parent = x;
}

void fixViolation(struct Node **root, struct Node *z) {
    while (z != *root && z->parent->color == 'R') {
        if (z->parent == z->parent->parent->left) {
            struct Node *y = z->parent->parent->right;
            if (y != NULL && y->color == 'R') {
                z->parent->color = 'B';
                y->color = 'B';
                z->parent->parent->color = 'R';
                z = z->parent->parent;
            } else {
                if (z == z->parent->right) {
                    z = z->parent;
                    leftRotate(root, z);
                }
                z->parent->color = 'B';
                z->parent->parent->color = 'R';
                rightRotate(root, z->parent->parent);
            }
        } else {
            struct Node *y = z->parent->parent->left;
            if (y != NULL && y->color == 'R') {
                z->parent->color = 'B';
                y->color = 'B';
                z->parent->parent->color = 'R';
                z = z->parent->parent;
            } else {
                if (z == z->parent->left) {
                    z = z->parent;
                    rightRotate(root, z);
                }
                z->parent->color = 'B';
                z->parent->parent->color = 'R';
                leftRotate(root, z->parent->parent);
            }
        }
    }
    (*root)->color = 'B';
}

struct Node *insertNode(struct Node *root, int data) {
    struct Node *newNode = createNode(data);
    struct Node *x = root;
    struct Node *y = NULL;

    while (x != NULL) {
        y = x;
        if (newNode->data < x->data)
            x = x->left;
        else
            x = x->right;
    }

    newNode->parent = y;
    if (y == NULL)
        root = newNode;
    else if (newNode->data < y->data)
        y->left = newNode;
    else
        y->right = newNode;

    fixViolation(&root, newNode);

    return root;
}

void inorderTraversal(struct Node *root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d(%c) ", root->data, root->color);
        inorderTraversal(root->right);
    }
}

void printTree(struct Node *root, int space) {
    if (root == NULL)
        return;

    space += 5;

    printTree(root->right, space);

    printf("\n");
    for (int i = 5; i < space; i++)
        printf(" ");

    printf("%d(%c)\n", root->data, root->color);

    printTree(root->left, space);
}


int main() {
    struct Node *root = NULL;
    root = insertNode(root, 7);
    root = insertNode(root, 3);
    root = insertNode(root, 18);
    root = insertNode(root, 10);
    root = insertNode(root, 22);
    root = insertNode(root, 8);
    root = insertNode(root, 11);

    printf("Inorder Traversal: ");
    inorderTraversal(root);
    printf("\n\nTree Structure:\n");
    printTree(root, 0);

    return 0;
}
