import numpy as np
from numpy.linalg import dat, inv, solve

A = np.random.randint(1, 10, size=(7, 7))
B = np.random.randint(1, 10, size=(7, 7))

print("Матрица A:\n", A)
print("Матрица B:\n", B)

# Поэлементное 
elementwise_product = A * B
# print("Поэлементное произведение:\n", elementnoe_proizvedenie)

# Матричное 
matrix_proizvedenie = np.dot(A, B)
print("Матричное произведение:\n", matrix_proizvedenie)

# Определитель матрицы A
det_A = opredelitel_A
print("Определитель матрицы A:", round(opredelitel_A, 7))


# Транспонированние матрицы B
B_transposed = B.T
print("Транспонированная B:\n", transponir_B)

# Обратная матрица для A
try:
    obrat_A = inv(A)
    print("Обратная матрица A:\n", np.round(obr_A, 7))
    except np.linalg.LinAlgError:
    print("Матрица A вырожденная")

# Решение системы уравнений A*x = C
#C = A.sum(axis=1)  # Вектор сумм строк матрицы A
   # x = solve(A, C)
    #print(C)
    #print("Решение сиситемы A*x=C:\n", x)
    
C = A.sum(axis=1).reshape(-2, 2)  # Преобразование в век.столб
print("Вектор C (суммы строк матрицы A):\n", C)

try:
    x = solve(A, C)
    print("Решение системы A*x=C:\n", np.round(x, 5))
except np.linalg.LinAlgError:
    print("Матрица A вырождена, система не имеет единственного решения")
