"""
Topic   : Valley Count & Array Rotation
Date    : December 17, 2025
Author  : Chaitanya

Note    : This code was originally placed in matrix_in_python.py
          but is unrelated to matrices — it belongs here with
          algorithmic / competitive coding problems.
"""

# ===========================================================
# PROBLEM 1: Counting Valleys (HackerRank-style)
# ===========================================================

"""
A valley is a sequence of steps below sea level that starts with
a downward step ("D") from sea level and ends when you return to
sea level (elevation == 0 after coming back up).
"""


def valley_count(n, path):
    """
    Count the number of valley sequences in the hike path.

    Args:
        n    : number of steps (length of path)
        path : string of "U" (up) and "D" (down) steps

    Returns:
        int : number of valleys
    """
    elevation = 0       # current height from sea level (0 = sea level)
    count = 0           # number of valleys completed

    for step in path:
        if step == "U":
            elevation += 1
            if elevation == 0:    # just came back to sea level
                count += 1        # completed one valley
        else:
            elevation -= 1

    return count


n = 8
path = "UDDDUDUU"
print(f"Valley count: {valley_count(n, path)}")

# ===========================================================
# PROBLEM 2: Counting Mountains
# ===========================================================

"""
A mountain is a sequence of steps ABOVE sea level that starts
with an upward step ("U") from sea level and ends when you
return to sea level.
"""


def count_mountains(path):
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


result = count_mountains("UDUUUDDD")
print(f"Number of mountains: {result}")

# ===========================================================
# PROBLEM 3: Rotate Array Left by d Positions
# ===========================================================

"""
Left rotation by d: shift all elements d positions to the left.
Elements that fall off the left end wrap around to the right.
Example: [1,2,3,4,5], d=2 → [3,4,5,1,2]
"""


def rotate_left(lst, d):
    n = len(lst)
    if d > n:
        d = d % n           # handle d > n
    return lst[d:] + lst[:d]


lst = [1, 2, 3, 4, 5]
d = 3
print(f"Rotated array (left by {d}):", rotate_left(lst, d))

lst = [1, 2, 3, 4, 5, 6]
d = 4
print(f"Rotated array (left by {d}):", rotate_left(lst, d))
