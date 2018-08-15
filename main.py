from __future__ import print_function
import os
import sys
import struct
import numpy as np
import argparse
import quat_utils
import generators



def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


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


def sformat(a):
    return "%.8f" % a
    if a < 0:
        return ("%.8f" % a).rjust(13)
    else:
        return (" %.8f" % a).rjust(13)


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


def parse_arguments(gdict):

    parser = argparse.ArgumentParser(description='Create a quaternion set with a specified Laue group and granularity')
    parser.add_argument("lauegroup", help="Laue group of orientation set")
    parser.add_argument("alpha", help="granularity of output set")
    parser.add_argument("outputformat")
    parser.add_argument('--weights', action='store_true', help='include point weights (Voronoi cell volumes)')
    args = parser.parse_args()

    target_group = args.lauegroup.upper()
    if target_group not in gdict.keys():
        ordered = sorted(gdict.keys())
        ordered[-1], ordered[-2] = ordered[-2], ordered[-1]
        eprint("Input error:")
        eprint("Laue group must be one of [%s]" % (", ".join(["'%s'" % e for e in ordered])))
        return None

    target_alpha = args.alpha
    target_alpha = int(round(float(target_alpha)))
    if target_alpha not in [1, 2, 3, 4, 5]:
        eprint("Input error:")
        eprint("Alpha must be one of: [1, 2, 3, 4, 5]")
        return None

    formats = ["quaternion", "q", "euler", "e", "matrix", "m"]
    output_format = args.outputformat.lower()
    if output_format not in formats:
        eprint("Input error:")
        eprint("Ouput format must be one of [%s]" % (', '.join(["'%s'" % e for e in formats])))
        return None

    index = formats.index(output_format)
    output_format = formats[index - index % 2]
    include_weights = args.weights
    return target_group, target_alpha, output_format, include_weights


def run():

    #get arguments from command line
    gdict = generators.generator_dict
    arguments = parse_arguments(gdict)
    if arguments is None:
        return

    target_group, target_alpha, output_format, include_weights = arguments
    subset, superset, map_indices = gdict[target_group]

    #construct data set
    folder = 'data'
    basis_file, alpha = find_basis_file(folder, superset, target_alpha)
    basis_points, basis_weights = read_points(os.path.join(folder, basis_file))

    mapped_points, mapped_weights = quat_utils.map_points_out(basis_points, basis_weights, superset, subset, map_indices)

    if output_format == 'matrix':
        mapped_points = np.array([quat_utils.quaternion_to_rotation_matrix(q).reshape(-1) for q in mapped_points])

    if output_format == 'euler':
        mapped_points = np.array([np.rad2deg(quat_utils.quaternion_to_euler(q)) for q in mapped_points])

    data = mapped_points
    if include_weights:
        data = np.concatenate((mapped_points.T, [mapped_weights])).T

    #print data set
    print(output_format)
    print(len(data))
    for line in data:
        print(" " + " ".join([sformat(e) for e in line]))

if __name__ == "__main__":
    run()

