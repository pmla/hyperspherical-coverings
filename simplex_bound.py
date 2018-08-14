import numpy as np
import scipy.optimize
import regular_simplex


def theta_to_edge_length(theta):
    cost = np.cos(theta)
    return np.arccos((4 * cost**2 - 1) / 3.0)


def solid_angle_fraction(theta):

    cost = np.cos(theta)
    alpha = np.arccos((4 * cost**2 - 1) / (8 * cost**2 + 1))
    return (3 * alpha - np.pi) / (4 * np.pi)


def calculate_n(r):

    l = theta_to_edge_length(r)
    volume = regular_simplex.calculate_volume(l)
    return 8 * np.pi**2 * solid_angle_fraction(r) / volume


def evalfunc(args, n):
    r = args
    return abs(n - calculate_n(r))


def find_r(n):

    thetamin = 1E-8
    thetamax = np.pi / 2
    result = scipy.optimize.fminbound(evalfunc, thetamin, thetamax, args=(n,), xtol=1E-09, maxfun=float("inf"), full_output=1, disp=0)
    return result[0]

