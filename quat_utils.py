import numpy as np


def flip_up(q):
    if q[0] < 0:
        q = -q
    return q

def multiply(r, a):

    b0 = r[0] * a[0] - r[1] * a[1] - r[2] * a[2] - r[3] * a[3]
    b1 = r[0] * a[1] + r[1] * a[0] + r[2] * a[3] - r[3] * a[2]
    b2 = r[0] * a[2] - r[1] * a[3] + r[2] * a[0] + r[3] * a[1]
    b3 = r[0] * a[3] + r[1] * a[2] - r[2] * a[1] + r[3] * a[0]
    return flip_up(np.array([b0, b1, b2, b3]))

def multiply_first_component(r, a):

    return r[0] * a[0] - r[1] * a[1] - r[2] * a[2] - r[3] * a[3]

def rotate_into_fundamental_zone(q, generators):

    index = np.argmax([abs(multiply_first_component(q, g)) for g in generators])
    return multiply(q, generators[index])

def map_points_out(basis_points, basis_weights, superset, subset, map_indices):

    assert( len(map_indices) * len(subset) == len(superset) )

    superset = np.array(superset)
    subset = np.array(subset)

    mapped_points = []
    mapped_weights = []
    for g in superset[map_indices]:
        for b, w in zip(basis_points, basis_weights):
            r = multiply(b, g)
            r = rotate_into_fundamental_zone(r, subset)
            mapped_points += [r]
            mapped_weights += [w]

    return np.array(mapped_points), np.array(mapped_weights)

def to_rotation_matrix(q):

    a, b, c, d = q

    u0 = a*a + b*b - c*c - d*d
    u1 = 2*b*c - 2*a*d
    u2 = 2*b*d + 2*a*c

    u3 = 2*b*c + 2*a*d
    u4 = a*a - b*b + c*c - d*d
    u5 = 2*c*d - 2*a*b

    u6 = 2*b*d - 2*a*c
    u7 = 2*c*d + 2*a*b
    u8 = a*a - b*b - c*c + d*d

    return np.array([[u0, u1, u2], [u3, u4, u5], [u6, u7, u8]])

