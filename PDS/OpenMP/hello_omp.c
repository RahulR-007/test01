#include <stdio.h>
#include <omp.h>
int main(void) {
    printf("OpenMP Parallel Programming\n");
    #pragma omp parallel
    {
        printf("Hello from thread %d\n", omp_get_thread_num());
    }
    return 0;
}
