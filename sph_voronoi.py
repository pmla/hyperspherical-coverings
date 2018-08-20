import numpy as np
from numpy.core.umath_tests import inner1d


def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)


def calculate_voronoi_vertices(qs):

    u = qs[:,1] - qs[:,0]
    v = qs[:,2] - qs[:,0]
    w = qs[:,3] - qs[:,0]

    p0 = +u[:,1] * (v[:,2] * w[:,3] - v[:,3] * w[:,2])\
         -u[:,2] * (v[:,1] * w[:,3] - v[:,3] * w[:,1])\
         +u[:,3] * (v[:,1] * w[:,2] - v[:,2] * w[:,1])

    p1 = -u[:,0] * (v[:,2] * w[:,3] - v[:,3] * w[:,2])\
         +u[:,2] * (v[:,0] * w[:,3] - v[:,3] * w[:,0])\
         -u[:,3] * (v[:,0] * w[:,2] - v[:,2] * w[:,0])

    p2 = +u[:,0] * (v[:,1] * w[:,3] - v[:,3] * w[:,1])\
         -u[:,1] * (v[:,0] * w[:,3] - v[:,3] * w[:,0])\
         +u[:,3] * (v[:,0] * w[:,1] - v[:,1] * w[:,0])

    p3 = -u[:,0] * (v[:,1] * w[:,2] - v[:,2] * w[:,1])\
         +u[:,1] * (v[:,0] * w[:,2] - v[:,2] * w[:,0])\
         -u[:,2] * (v[:,0] * w[:,1] - v[:,1] * w[:,0])

    p = np.array([p0, p1, p2, p3]).T

    dots = inner1d(p, qs[:,0])
    signs = 2 * (dots > 0) - 1
    p = p * np.expand_dims(signs, axis=-1)

    return normalized(p)

