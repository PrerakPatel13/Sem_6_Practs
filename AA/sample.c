#include <stdio.h>

int main() {
    int myArray[5];

    for (int i = 0; i < 5; i++) {
        myArray[i] = i * 2;
    }

    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += myArray[i];
    }

    printf("Sum of array elements: %d\n", sum);

    return 0;
}


