"""Basic states and operators for the two-qubit Ising model."""

import numpy as np
from numpy.typing import NDArray


ComplexArray = NDArray[np.complex128]


# ----------------------------------------------------------------------
# Single-qubit basis states
# ----------------------------------------------------------------------

KET_0: ComplexArray = np.array(
    [1.0, 0.0],
    dtype=complex,
)

KET_1: ComplexArray = np.array(
    [0.0, 1.0],
    dtype=complex,
)


# ----------------------------------------------------------------------
# Single-qubit operators
# ----------------------------------------------------------------------

I: ComplexArray = np.eye(2, dtype=complex)

X: ComplexArray = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
    ],
    dtype=complex,
)

Y: ComplexArray = np.array(
    [
        [0.0, -1.0j],
        [1.0j, 0.0],
    ],
    dtype=complex,
)

Z: ComplexArray = np.array(
    [
        [1.0, 0.0],
        [0.0, -1.0],
    ],
    dtype=complex,
)


# ----------------------------------------------------------------------
# Two-qubit computational basis
# Ordered as |00>, |01>, |10>, |11>
# ----------------------------------------------------------------------

KET_00: ComplexArray = np.kron(KET_0, KET_0)
KET_01: ComplexArray = np.kron(KET_0, KET_1)
KET_10: ComplexArray = np.kron(KET_1, KET_0)
KET_11: ComplexArray = np.kron(KET_1, KET_1)

COMPUTATIONAL_BASIS: tuple[ComplexArray, ...] = (
    KET_00,
    KET_01,
    KET_10,
    KET_11,
)

BASIS_LABELS: tuple[str, ...] = (
    "|00>",
    "|01>",
    "|10>",
    "|11>",
)


# ----------------------------------------------------------------------
# Two-qubit Pauli operators
#
# The first tensor factor corresponds to the first bit in |q0 q1>
# under the NumPy convention used in the analytical calculations.
# ----------------------------------------------------------------------

X0: ComplexArray = np.kron(X, I)
X1: ComplexArray = np.kron(I, X)

Y0: ComplexArray = np.kron(Y, I)
Y1: ComplexArray = np.kron(I, Y)

Z0: ComplexArray = np.kron(Z, I)
Z1: ComplexArray = np.kron(I, Z)

ZZ: ComplexArray = Z0 @ Z1

MZ: ComplexArray = 0.5 * (Z0 + Z1)
