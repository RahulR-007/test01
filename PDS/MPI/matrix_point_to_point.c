#include <mpi.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
    int rank;
    int A[2][2] = {{1,2},{3,4}};
    int B[2][2] = {{5,6},{7,8}};
    int C[2][2];
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0) {
        for (int i = 0; i < 2; i++) {
            int result[2];
            MPI_Send(A[i], 2, MPI_INT, 1, 0, MPI_COMM_WORLD);
            MPI_Send(B, 4, MPI_INT, 1, 1, MPI_COMM_WORLD);
            MPI_Recv(result, 2, MPI_INT, 1, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            for (int j = 0; j < 2; j++) C[i][j] = result[j];
        }
        printf("Result Matrix:\n");
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) printf("%d ", C[i][j]);
            printf("\n");
        }
    } else if (rank == 1) {
        for (int i = 0; i < 2; i++) {
            int row[2], b[4], result[2];
            MPI_Recv(row, 2, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            MPI_Recv(b, 4, MPI_INT, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            for (int j = 0; j < 2; j++) {
                result[j] = 0;
                for (int k = 0; k < 2; k++) result[j] += row[k] * b[k*2+j];
            }
            MPI_Send(result, 2, MPI_INT, 0, 2, MPI_COMM_WORLD);
        }
    }
    MPI_Finalize();
    return 0;
}
