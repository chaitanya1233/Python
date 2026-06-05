"""
Topic   : LeetCode-Style Problems 01 — Arrays, Searching & Matrices
Date    : December 18, 2025
Author  : Chaitanya
"""

# ===========================================================
# PROBLEM 1: Valley Count — Track Below Sea Level
# ===========================================================

def valley_count(path):
    """Count valleys: sequences below sea level."""
    elevation = 0
    count = 0
    for step in path:
        if step == "U":
            elevation += 1
        else:
            elevation -= 1
            if elevation == 0:
                count += 1
    return count

print("Valley count:", valley_count("UDDDUDUU"))

# ===========================================================
# PROBLEM 2: Mountain Count
# ===========================================================

def count_mountains(path):
    """Count mountains: sequences above sea level."""
    elevation = 0
    mountains = 0
    for step in path:
        if step == "U":
            elevation += 1
        else:
            elevation -= 1
            if elevation == 0:
                mountains += 1
    return mountains

mountain_count = count_mountains("UDUUUDDD")
print(f"Number of mountains: {mountain_count}")

# ===========================================================
# PROBLEM 3: Left Rotate an Array by d Positions
# ===========================================================

def rotate_array(arr, d):
    n = len(arr)
    if d > n:
        d = d % n
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5, 6]
d = 4
rotated_arr = rotate_array(arr, d)
print("The rotated array is:", rotated_arr)

# ===========================================================
# PROBLEM 4: Print and Access Matrix Elements
# ===========================================================

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rows = len(mat)
cols = len(mat[0])

for i in range(rows):
    for j in range(cols):
        print(f"The element at index mat[{i}][{j}] is {mat[i][j]}")

# ===========================================================
# PROBLEM 5: Print Diagonal Elements of a Matrix
# ===========================================================

print("The diagonal elements are:")
for i in range(rows):
    for j in range(cols):
        if i == j:
            print(mat[i][j])

# ===========================================================
# PROBLEM 6: Matrix Addition
# ===========================================================

mat1 = [[1, 2, 3],
        [3, 4, 5],
        [6, 7, 8]]

mat2 = [[1, 2, 4],
        [3, 4, 5],
        [5, 6, 7]]

add = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        add[i][j] = mat1[i][j] + mat2[i][j]

print("Matrix addition result:", add)

# ===========================================================
# PROBLEM 7: Sparse Matrix Check
# ===========================================================

matrix = [[0, 0, 0],
          [0, 3, 0],
          [3, 0, 0]]

rows = len(matrix)
cols = len(matrix[0])
count = sum(1 for i in range(rows) for j in range(cols) if matrix[i][j] == 0)

if (rows * cols) / 2 < count:
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")
