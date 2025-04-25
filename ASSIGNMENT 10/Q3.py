"""3. A magic square is an N×N grid of numbers in which the entries in each row, column and
main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
N=4, 5, 6, 7, 8"""

import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        i_new, j_new = (i - 1) % n, (j + 1) % n
        if magic_square[i_new, j_new] != 0:
            i += 1
        else:
            i, j = i_new, j_new

    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                magic_square[i, j] = n * n + 1 - magic_square[i, j]
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square_size = half_n * half_n
    sub_square = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)

    for i in range(half_n):
        for j in range(half_n):
            magic_square[i, j] = sub_square[i, j]
            magic_square[i + half_n, j + half_n] = sub_square[i, j] + sub_square_size
            magic_square[i + half_n, j] = sub_square[i, j] + 2 * sub_square_size
            magic_square[i, j + half_n] = sub_square[i, j] + 3 * sub_square_size

    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(k):
            magic_square[i, j], magic_square[i + half_n, j] = (
                magic_square[i + half_n, j],
                magic_square[i, j],
            )
        for j in range(n - k, n):
            magic_square[i, j], magic_square[i + half_n, j] = (
                magic_square[i + half_n, j],
                magic_square[i, j],
            )

    for i in range(k):
        magic_square[i, k], magic_square[i + half_n, k] = (
            magic_square[i + half_n, k],
            magic_square[i, k],
        )

    return magic_square

def print_magic_square(n, magic_square):
    print(f"Magic Square for N={n}:")
    print(magic_square)
    print(f"Sum of each row/column/diagonal: {n * (n**2 + 1) // 2}")
    print()


for n in [4, 5, 6, 7, 8]:
    if n % 2 == 1:
        magic_square = generate_odd_magic_square(n)
    elif n % 4 == 0:
        magic_square = generate_doubly_even_magic_square(n)
    else:
        magic_square = generate_singly_even_magic_square(n)
    print_magic_square(n, magic_square)