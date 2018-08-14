import numpy as np
import scipy.special


def ei(t):
    return np.exp(1j * t)


def verify_solution(t, z0):

    sol = (ei(3*t) + z0)**4 / ((1 - z0) * (ei(4*t) - z0)**3)

    if abs(np.real(sol) - 1.0) > 1E-3:
        raise Exception("real part not 1")
    if abs(np.imag(sol)) > 1E-3:
        raise Exception("imaginary part not 0")


def Li2(x):
    return scipy.special.spence(1 - x)


def calculate_volume(l):

    t = np.arccos(np.cos(l) / (2*np.cos(l) + 1))
    sint = np.sin(t)
    cost = np.cos(t)

    q2 = 3*ei(-2*t) + 4*ei(-3*t) + ei(-6*t)
    z0 = (-6*sint**2 + 2 * np.sqrt((cost+1)**3 * (1 - 3*cost))) / q2

    verify_solution(t, z0)

    L = 0.5 * (Li2(z0) + 3*Li2(z0 * ei(-4*t)) - 4*Li2(-z0 * ei(-3*t)) - 3*t**2)
    vol = -np.real(L) + np.pi * (np.angle(-q2) + 3 * t) - 1.5*np.pi**2
    vol = vol % (2 * np.pi**2)
    return vol

