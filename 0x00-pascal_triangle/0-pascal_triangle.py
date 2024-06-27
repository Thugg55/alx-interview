"""
auth: PUTECH
pascal-triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    tech = []
    if n > 0:
        for i in range(1, n + 1):
            step = []
            R = 1
            for j in range(1, i + 1):
                step.append(R)
                R = R * (i - j) // j
            tech.append(level)
    return tech
