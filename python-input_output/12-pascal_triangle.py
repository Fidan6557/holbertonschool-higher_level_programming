#!/usr/bin/python3
"""Technical interview preparation"""


def pascal_triangle(n):
    """a function about pascal triangle"""
    p = []
    if n <= 0:
        return p
    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(p[i-1][j-1]+p[i-1][j])
        if i > 0:
            row.append(1)
        p.append(row)
    return p
