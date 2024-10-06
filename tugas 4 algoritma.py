def input_matrix(rows, cols):
    matrix = []
    for i in range(rows): 
        row = list(map(int, input(f"input row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def multiply_matrices(A, B):
    mA = len(A)
    nA = len(A[0])
    mB = len(B)
    nB = len(B[0])
    
    C = [[0] * nB for _ in range(mA)]

    for i in range(mA):
        for j in range(nB):
            for k in range(nA):
                C[i][j] += A[i][k] * B[k][j]

    return C


mA = int(input("masukkan jumlah baris untuk matriks A"))
nA = int(input("masukkan jumlah kolom untuk matriks A"))
A = input_matrix(mA, nA)

mB = int(input("masukkan jumlah baris untuk matriks B"))
nB = int(input("masukkan jumlah kolom untuk matriks B"))
B = input_matrix(mB, nB)

if nA == mB:
    print("matriks tidak dapat dikalikan")
else:
    C = multiply_matrices(A, B)
    print("hasil perkalian matriks C")
    print_matrix(C)


