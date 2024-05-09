#include<stdio.h>

struct Stack{
    int table[100];
    int top;
};

struct Stack push(struct Stack p, int x){
    p.top+=1;
    p.table[p.top] = x;
    return p;
}

struct Stack pop(struct Stack p){
    p.top-=1;
    return p;
}

struct Stack multipop(struct Stack p, int x){
    p.top-=x;
    return p;
}

void display(struct Stack p){
    for (int i=0; i<=p.top; i++){
        printf("%d ", p.table[i]);
    }
    printf("\n");
}

void main(){
    struct Stack s;
    s.top=-1;
    s = push(s, 1);
    s = push(s, 2);
    s = push(s, 3);
    s = push(s, 4);
    display(s);
    s = push(s, 5);
    for (int i=6; i<15; i++){
        s = push(s, i);
    }
    display(s);
    s = pop(s);
    s = multipop(s, 2);
    display(s);
    s = pop(s);
    s = multipop(s, 9);
    display(s);
}