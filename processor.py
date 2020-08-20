def read_matrices(operation):
    if operation == "1" or operation == "3":
        matrix_1_rows, matrix_1_columns = input("Enter size of first matrix: ").split()
        print("Enter first matrix:")
        matrix_1 = [[float(j) for j in input().split()] for _ in range(int(matrix_1_rows))]
        matrix_2_rows, matrix_2_columns = input("Enter size of second matrix: ").split()
        print("Enter second matrix:")
        matrix_2 = [[float(j) for j in input().split()] for _ in range(int(matrix_2_rows))]
        return matrix_1_rows, matrix_1_columns, matrix_2_rows, matrix_2_columns, matrix_1, matrix_2
    elif operation == "2":
        matrix_rows, matrix_columns = input("Enter size of matrix: ").split()
        print("Enter matrix:")
        matrix = [[float(j) for j in input().split()] for _ in range(int(matrix_rows))]
        constant = float(input("Enter constant: "))
        return matrix_rows, matrix_columns, matrix, constant
    else:
        matrix_rows, matrix_columns = input("Enter matrix size: ").split()
        print("Enter matrix:")
        matrix = [[float(j) for j in input().split()] for _ in range(int(matrix_rows))]
        return matrix_rows, matrix_columns, matrix


def print_matrix(number_of_rows, matrix):
    rounded_matrix = [[round(matrix[i][j], 4) for j in range(len(matrix[0]))] for i in range(int(number_of_rows))]
    print("The result is:")
    for row in range(len(rounded_matrix)):
        print(" ".join(map(str, rounded_matrix[row])))
    print()


def transpose_matrix(m_rows, m_columns, matrix, transposition_type):
    if transposition_type == "1":  # Main diagonal
        matrix_t = [[matrix[j][i] for j in range(int(m_rows))] for i in range(int(m_columns))]
        return matrix_t
    elif transposition_type == "2":  # Side diagonal
        matrix_t = [[matrix[j][i] for j in range(int(m_rows)-1, -1, -1)] for i in range(int(m_columns)-1, -1, -1)]
        return matrix_t
    elif transposition_type == "3":  # Vertical line
        matrix_t = [[matrix[i][j] for j in range(int(m_columns)-1, -1, -1)] for i in range(int(m_rows))]
        return matrix_t
    else:  # Horizontal line
        matrix_t = [[matrix[i][j] for j in range(int(m_columns))] for i in range(int(m_rows)-1, -1, -1)]
        return matrix_t


def calculate_determinant(m_rows, m_columns, m):
    if m_rows != m_columns:
        print("Unable to calculate determinant of a non-square matrix\n")
        return

    if int(m_columns) == 1:
        return m[0][0]
    elif int(m_columns) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        determinant = 0
        for column in range(int(m_columns)):
            cofactor = calculate_cofactor(0, column, int(m_rows), int(m_columns), m)
            determinant += m[0][column] * cofactor
        return determinant


def calculate_cofactor(row, column, m_rows, m_columns, matrix):
    minor_matrix = [[matrix[i][j] for j in range(m_columns) if j != column] for i in range(m_rows) if i != row]
    minor = calculate_determinant(len(minor_matrix), len(minor_matrix), minor_matrix)
    cofactor = ((-1) ** ((column + 1) + (row + 1))) * minor
    return cofactor


def invert_matrix(m_rows, m_columns, m):
    if m_rows != m_columns or calculate_determinant(m_rows, m_columns, m) == 0:
        print("Matrix is not invertible\n")
    else:
        deter = calculate_determinant(m_rows, m_columns, m)
        cofactor_matrix = []
        for row in range(int(m_rows)):
            cofactor_matrix.append([])
            for column in range(int(m_columns)):
                cofactor = calculate_cofactor(row, column, int(m_rows), int(m_columns), m)
                cofactor_matrix[row].append(cofactor)
        adjunct_matrix = transpose_matrix(int(m_rows), int(m_columns), cofactor_matrix, "1")
        inverse_matrix = [[adjunct_matrix[i][j] / deter for j in range(int(m_columns))] for i in range(int(m_rows))]
        return len(inverse_matrix), inverse_matrix


def dot_product(vector_1, vector_2):
    dot_p = 0
    for i in range(len(vector_1)):
        dot_p += vector_1[i] * vector_2[i]
    return dot_p


using_matrix_processor = True
while using_matrix_processor:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n"
          "4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    inp_operation = input("Your choice: ")
    if inp_operation == "1":
        A_rows, A_columns, B_rows, B_columns, A, B = read_matrices(inp_operation)
        if A_rows == B_rows and A_columns == B_columns:
            A_plus_B = [[A[i][j] + B[i][j] for j in range(int(A_columns))] for i in range(int(A_rows))]
            print_matrix(A_rows, A_plus_B)
        else:
            print("The operation cannot be performed.\n")
    elif inp_operation == "2":
        M_rows, M_columns, M, c = read_matrices(inp_operation)
        c_times_M = [[M[i][j] * c for j in range(int(M_columns))] for i in range(int(M_rows))]
        print_matrix(M_rows, c_times_M)
    elif inp_operation == "3":
        A_rows, A_columns, B_rows, B_columns, A, B = read_matrices(inp_operation)
        if A_columns == B_rows:
            B_t = transpose_matrix(B_rows, B_columns, B, "1")
            A_times_B = [[dot_product(A[n], B_t[k]) for k in range(int(B_columns))] for n in range(int(A_rows))]
            print_matrix(A_rows, A_times_B)
        else:
            print("The operation cannot be performed.\n")
    elif inp_operation == "4":
        print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        transpose_operation = input("Your choice: ")
        M_rows, M_columns, M = read_matrices(inp_operation)
        M_t = transpose_matrix(M_rows, M_columns, M, transpose_operation)
        if transpose_operation == "1" or transpose_operation == "2":
            print_matrix(M_columns, M_t)
        else:
            print_matrix(M_rows, M_t)
    elif inp_operation == "5":
        M_rows, M_columns, M = read_matrices(inp_operation)
        det = calculate_determinant(M_rows, M_columns, M)
        print(f"The result is:\n{det}\n")
    elif inp_operation == "6":
        M_rows, M_columns, M = read_matrices(inp_operation)
        inv_M_rows, inv_M = invert_matrix(M_rows, M_columns, M)
        print_matrix(inv_M_rows, inv_M)
    else:
        using_matrix_processor = False
        break
