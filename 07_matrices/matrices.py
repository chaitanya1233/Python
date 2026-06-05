"""
Topic   : Matrices in Python (List of Lists)
Date    : December 17, 2025
Author  : Chaitanya

Note    : Valley count and array rotation problems (also in this session)
          have been moved to 11_competitive_coding/valley_count_and_array_rotation.py
"""

# ===========================================================
# SECTION 1: Matrix Representation & Access
# ===========================================================

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(mat)

rows = len(mat)
cols = len(mat[0])
print("The number of rows are:", rows)
print("The number of columns are:", cols)

# Access each element
for i in range(rows):
    for j in range(cols):
        print(f"The element at mat[{i}][{j}] is {mat[i][j]}")

# ===========================================================
# SECTION 2: Matrix Addition
# ===========================================================

# To add two matrices their rows and columns must be equal
mat1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

mat2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

rows = len(mat1)
cols = len(mat1[0])

for i in range(rows):
    for j in range(cols):
        result[i][j] = mat1[i][j] + mat2[i][j]

print("Matrix Addition Result:")
print(result)

# ===========================================================
# SECTION 3: Diagonal Elements
# ===========================================================

mat4 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

rows = len(mat4)
cols = len(mat4[0])

print("The diagonal elements are:")
for i in range(rows):
    for j in range(cols):
        if i == j:
            print(mat4[i][j])

# ===========================================================
# SECTION 4: Sparse Matrix Check
# ===========================================================

"""
A matrix is sparse if more than half of its elements are zero.
"""

mat = [[0, 0, 2],
       [1, 2, 54],
       [0, 32, 20]]

rows = len(mat)
cols = len(mat[0])
count = 0

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == 0:
            count += 1

total_elements = rows * cols
print("Total elements:", total_elements)
print("Zero count:", count)

if count > total_elements / 2:
    print("The given matrix is sparse.")
else:
    print("The given matrix is not sparse.")
