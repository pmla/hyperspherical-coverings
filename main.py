from __future__ import print_function
import struct
import numpy as np
import argparse
import os

import quat_utils
import generators


def read_points(path):
    s = open(path, 'rb').read()
    if len(s) % 20 != 0:
        raise Exception("wrong filesize for a basis quaternion set")

    n = len(s) // 20
    data = struct.unpack(5 * n * 'f', s)
    data = np.array(data).reshape((n, 5))
    qs = np.array(data[:,:4]).astype(np.double)
    ws = np.array(data[:,4]).astype(np.double)
    return qs, ws

def write_data(data, path):

    data = list(data.reshape(-1))
    n = len(data)
    s = struct.pack(n * 'f', *data)
    open(path, 'wb').write(s)

def sformat(a):
    if a < 0:
        return "%.12f" % a
    else:
        return " %.12f" % a

def find_basis_file(data_folder, superset, target_alpha):

    files = os.listdir(data_folder)
    files = [f for f in files if f.startswith('fundamental_g=') and f.endswith(".dat")]

    #file name format: fundamental_g=O24_n=6291456_alpha=0.986.dat
    for f in files:
        root = os.path.splitext(f)[0]
        stats = root.split('_')[1:]
        stats = dict([e.split('=') for e in stats])
        g = stats['g']
        alpha = float(stats['alpha'])
        if abs(alpha - target_alpha) < 0.05:
            if g == 'O24' and superset == generators.generator_laue_O:
                return f, alpha
            if g == 'D6' and superset == generators.generator_laue_D6:
                return f, alpha

    raise Exception("basis file not present")

def go(target_alpha, target_group, include_weights=False, convert_to_matrix=False, print_to_stdout=False):

    subset, superset, map_indices = gdict[target_group]

    folder = 'data'
    basis_file, alpha = find_basis_file(folder, superset, target_alpha)
    basis_points, basis_weights = read_points(os.path.join(folder, basis_file))

    mapped_points, mapped_weights = quat_utils.map_points_out(basis_points, basis_weights, superset, subset, map_indices)

    if convert_to_matrix:
        mapped_points = np.array([quat_utils.to_rotation_matrix(q).reshape(-1) for q in mapped_points])

    data = mapped_points
    if include_weights:
        data = np.concatenate((mapped_points.T, [mapped_weights])).T

    if print_to_stdout:
        for line in data:
            print(" ".join([sformat(e) for e in line]))
    else:
        #file name format: points_g=O24_n=6291456_alpha=0.986.dat
        filename = 'points_g=%s_n=%d_alpha=%.3f.dat' % (target_group, len(data), alpha)
        write_data(data, filename)
        print("wrote file:", filename)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Create a quaternion set with a specified Laue group and granularity')
    parser.add_argument("lauegroup")
    parser.add_argument("alpha")
    parser.add_argument('--weights', action='store_true', help='include point weights (Voronoi cell volumes)')
    parser.add_argument('--matrix', action='store_true', help='convert points to rotation matrices')
    parser.add_argument('--print', action='store_true', help='print to stdout rather than to a file')
    args = parser.parse_args()


    gdict = generators.generator_dict

    target_alpha = args.alpha
    target_alpha = int(round(float(target_alpha)))
    if target_alpha not in [1, 2, 3, 4, 5]:
        raise Exception("alpha must be one of: [1, 2, 3, 4, 5]")

    target_group = args.lauegroup
    target_group = target_group.upper()
    if target_group not in gdict.keys():
        raise Exception("Laue group must be one of [%s]" % (','.join(gdict.keys())))

    go(target_alpha, target_group, args.weights, args.matrix, args.print)

