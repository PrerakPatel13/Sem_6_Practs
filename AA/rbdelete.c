#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    char color;
    struct Node *left, *right, *parent;
};

// Function definition for transplant
void transplant(struct Node **root, struct Node *u, struct Node *v) {
    if (u->parent == NULL)
        *root = v;
    else if (u == u->parent->left)
        u->parent->left = v;
    else
        u->parent->right = v;
    if (v != NULL)
        v->parent = u->parent;
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
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->color = 'R';
    newNode->left = newNode->right = newNode->parent = NULL;

    struct Node *y = NULL;
    struct Node *x = root;

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

struct Node* findMinimum(struct Node* node) {
    while (node->left != NULL)
        node = node->left;
    return node;
}
void fixDoubleBlack(struct Node **root, struct Node *x) {
    while (x != *root && x->color == 'B') {
        if (x == x->parent->left) {
            struct Node *w = x->parent->right;
            if (w->color == 'R') {
                w->color = 'B';
                x->parent->color = 'R';
                leftRotate(root, x->parent);
                w = x->parent->right;
            }
            if (w->left->color == 'B' && w->right->color == 'B') {
                w->color = 'R';
                x = x->parent;
            } else {
                if (w->right->color == 'B') {
                    w->left->color = 'B';
                    w->color = 'R';
                    rightRotate(root, w);
                    w = x->parent->right;
                }
                w->color = x->parent->color;
                x->parent->color = 'B';
                w->right->color = 'B';
                leftRotate(root, x->parent);
                x = *root;  // Update x to root
            }
        } else {
            struct Node *w = x->parent->left;
            if (w->color == 'R') {
                w->color = 'B';
                x->parent->color = 'R';
                rightRotate(root, x->parent);
                w = x->parent->left;
            }
            if (w->right->color == 'B' && w->left->color == 'B') {
                w->color = 'R';
                x = x->parent;
            } else {
                if (w->left->color == 'B') {
                    w->right->color = 'B';
                    w->color = 'R';
                    leftRotate(root, w);
                    w = x->parent->left;
                }
                w->color = x->parent->color;
                x->parent->color = 'B';
                w->left->color = 'B';
                rightRotate(root, x->parent);
                x = *root;  // Update x to root
            }
        }
    }
    x->color = 'B';
}
struct Node *deleteNode(struct Node *root, int data) {
    printf("Deleting node with data: %d\n", data); // Debug message
    if (root == NULL) {
        printf("Root is NULL, returning...\n"); // Debug message
        return root;
    }

    struct Node *z = root;
    struct Node *x, *y;
    while (z != NULL) {
        if (data < z->data)
            z = z->left;
        else if (data > z->data)
            z = z->right;
        else
            break;
    }

    if (z == NULL) {
        printf("Node not found, returning...\n"); // Debug message
        return root;
    }

    char original_color = z->color;
    if (z->left == NULL) {
        x = z->right;
        transplant(&root, z, z->right);
    } else if (z->right == NULL) {
        x = z->left;
        transplant(&root, z, z->left);
    } else {
        y = findMinimum(z->right);
        original_color = y->color;
        x = y->right;
        if (y->parent == z)
            x->parent = y;
        else {
            transplant(&root, y, y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        transplant(&root, z, y);
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }

    printf("Node with data %d deleted successfully\n", data); // Debug message
    free(z);

    if (x != NULL && original_color == 'B') // Check if x is not NULL before fix-up
        fixDoubleBlack(&root, x);

    return root;
}


int main() {
    struct Node *root = NULL;
    root = insertNode(root, 83);
    root = insertNode(root, 77);
    root = insertNode(root, 86);
    root = insertNode(root, 15);
    root = insertNode(root, 93);

    printf("Inorder Traversal: ");
    inorderTraversal(root);
    printf("\n\nTree Structure:\n");
    printTree(root, 0);

    root = deleteNode(root, 83);
    printf("\nAfter deleting 83:\n");
    printf("Inorder Traversal: ");
    inorderTraversal(root);
    printf("\n\nTree Structure:\n");
    printTree(root, 0);

    return 0;
}
