# matrixprocessing.py
import numpy as np

def read_matrix():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix

def add_matrices():
    print("Enter size of first matrix:")
    matrix_A = read_matrix()
    print("Enter size of second matrix:")
    matrix_B = read_matrix()

    if np.shape(matrix_A) != np.shape(matrix_B):
        print("The operation cannot be performed.")
        return

    result = np.add(matrix_A, matrix_B)

    print("The result is:")
    print(result)

def multiply_matrix_by_constant():
    print("Enter size of matrix:")
    matrix = read_matrix()
    constant = float(input("Enter constant: "))

    result = np.multiply(matrix, constant)

    print("The result is:")
    print(result)

def multiply_matrices():
    print("Enter size of first matrix:")
    matrix_A = read_matrix()
    print("Enter size of second matrix:")
    matrix_B = read_matrix()

    if np.shape(matrix_A)[1] != np.shape(matrix_B)[0]:
        print("The operation cannot be performed.")
        return

    result = np.dot(matrix_A, matrix_B)

    print("The result is:")
    print(result)

def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    choice = input("Your choice: ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        return

    print("Enter matrix size:")
    matrix = read_matrix()

    if choice == "1":
        result = np.transpose(matrix)
    elif choice == "2":
        result = np.fliplr(np.flipud(matrix))
    elif choice == "3":
        result = np.fliplr(matrix)
    elif choice == "4":
        result = np.flipud(matrix)

    print("The result is:")
    print(result)

def calculate_determinant():
    print("Enter matrix size:")
    n, m = map(int, input().split())
    if n != m:
        print("The matrix must be square.")
        return

    print("Enter matrix:")
    matrix = read_matrix()

    determinant = np.linalg.det(matrix)

    print("The result is:")
    print(determinant)

def inverse_matrix():
    print("Enter matrix size:")
    n, m = map(int, input().split())
    if n != m:
        print("The matrix must be square.")
        return

    print("Enter matrix:")
    matrix = read_matrix()

    determinant = np.linalg.det(matrix)

    if determinant == 0:
        print("This matrix doesn't have an inverse.")
    else:
        inverse = np.linalg.inv(matrix)
        print("The result is:")
        print(inverse)

def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        choice = input("Your choice: ")
        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_matrix_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
