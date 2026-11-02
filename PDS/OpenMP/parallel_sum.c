#include <stdio.h>
#include <omp.h>
int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    int sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < 5; i++) sum += a[i];
    printf("Sum = %d\n", sum);
    return 0;
}
