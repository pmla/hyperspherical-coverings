from __future__ import print_function
import os
import argparse
import numpy as np
import scipy.spatial
import matplotlib.pyplot as plt
import matplotlib
from numpy.core.umath_tests import inner1d

import quat_utils
import sph_voronoi
import simplex_bound
import generators


label_size = 15
matplotlib.rcParams['xtick.labelsize'] = label_size



def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)


def misorientation(a, b):

    dots = inner1d(a, b)
    dots = np.minimum(1, np.maximum(-1, dots))
    return 2 * np.arccos(np.abs(dots))


def read_file(input_file):

    lines = open(input_file).read().split('\n')
    if len(lines) == 0:
        raise Exception("input file is empty")

    lines = [e for e in lines if len(e) > 1]

    input_format = lines[0]
    if input_format not in ['euler', 'quaternion', 'matrix']:
        raise Exception("invalid input format")

    num = int(lines[1])
    if num <= 0:
        raise Exception("input file contains no orientations")

    data = []
    for line in lines[2:]:
        data += [[float(e) for e in line.split()]]
    data = np.array(data)

    if input_format == 'quaternion':
        assert data.shape[1] >= 4
        data = data[:,:4]

    elif input_format == 'euler':
        assert data.shape[1] >= 3
        data = np.deg2rad(data)
        data = np.array([quat_utils.euler_to_quaternion(e[:3]) for e in data])

    elif input_format == 'matrix':
        assert data.shape[1] >= 9
        data = np.array([quat_utils.rotation_matrix_to_quaternion(e[:9].reshape((3,3))) for e in data])

    return data


def go(input_file, target_group, k, gdict):

    basis_points = read_file(input_file)
    gs, _, _ = gdict[target_group]

    mapped_points = []
    for g in gs:
        for b in basis_points:
            r = quat_utils.multiply(b, g)
            mapped_points += [r]
    mapped_points = np.array(mapped_points)


    qs = mapped_points
    n = len(qs)
    qs = np.concatenate((-qs, qs))

    #calculate a lower bound on the maximum error
    r = simplex_bound.find_r(2 * n)
    lower_bound = np.rad2deg(2 * r)

    #sample the error distribution
    tree = scipy.spatial.cKDTree(qs)
    ps = quat_utils.random_quaternions(k)
    _, indices = tree.query(ps)
    ms = misorientation(ps, qs[indices])

    #calculate the maximum error exactly (covering radius)
    simplices = scipy.spatial.ConvexHull(qs).simplices
    vs = sph_voronoi.calculate_voronoi_vertices(qs[simplices])
    rs = misorientation(vs, qs[simplices[:,0]])
    mmax = np.rad2deg(np.max(rs))

    print("maximum misorientation: %.2f degrees" % mmax)
    print("         simplex bound: %.2f degrees" % lower_bound)
    print("        optimality gap: %.2f%%" % (100 * (mmax / lower_bound - 1)))

    #plot the results
    counts, _, _, = plt.hist(np.rad2deg(ms), bins=200)
    plt.plot([lower_bound, lower_bound], [0, max(counts)], ls=':')
    plt.plot([mmax, mmax], [0, max(counts)], ls=':')
    plt.xlabel('Misorientation (degrees)', fontsize=label_size)
    plt.ylabel('Frequency', fontsize=15)
    plt.yticks([])
    plt.show()


def run():
    parser = argparse.ArgumentParser(description='Plot the error statistics of a set of orientations')
    parser.add_argument("inputfile", help="file containing orientations")
    parser.add_argument("lauegroup", help="Laue group of orientation set")
    parser.add_argument("k", help="number of error distribution samples")
    args = parser.parse_args()

    gdict = generators.generator_dict
    target_group = args.inputfile
    target_group = args.lauegroup.upper()
    if target_group not in gdict.keys():
        ordered = sorted(gdict.keys())
        ordered[-1], ordered[-2] = ordered[-2], ordered[-1]
        eprint("Input error:")
        eprint("Laue group must be one of [%s]" % (", ".join(["'%s'" % e for e in ordered])))
        return None

    input_file = args.inputfile
    k = int(args.k)
    assert k > 0
    go(input_file, target_group, k, gdict)


if __name__ == "__main__":
    run()
