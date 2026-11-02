#include <mpi.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
    int rank, size;
    int a[8] = {10,20,30,40,50,60,70,80};
    int local[2], local_sum = 0, total_sum = 0;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (size != 4) {
        if (rank == 0) printf("Run with exactly 4 processes.\n");
        MPI_Finalize();
        return 0;
    }
    MPI_Scatter(a, 2, MPI_INT, local, 2, MPI_INT, 0, MPI_COMM_WORLD);
    for (int i = 0; i < 2; i++) local_sum += local[i];
    MPI_Reduce(&local_sum, &total_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0) printf("Total Sum = %d\n", total_sum);
    MPI_Finalize();
    return 0;
}
