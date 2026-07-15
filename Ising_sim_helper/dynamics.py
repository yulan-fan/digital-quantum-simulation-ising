"""Exact dynamics and numerical diagnostics."""

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

from .operators import X0, X1, ZZ


ComplexArray = NDArray[np.complex128]


def build_hamiltonian(J: float, h: float) -> ComplexArray:
    """Construct the two-qubit transverse-field Ising Hamiltonian.

    H = -J Z0 Z1 - h (X0 + X1)
    """
    return -J * ZZ - h * (X0 + X1)


def exact_state(
    time: float,
    hamiltonian: ComplexArray,
    initial_state: ComplexArray,
) -> ComplexArray:
    """Calculate exact real-time evolution exp(-i H t)|psi(0)>."""
    return expm(-1.0j * hamiltonian * time) @ initial_state


def expectation_value(
    state: ComplexArray,
    operator: ComplexArray,
) -> float:
    """Calculate <psi|O|psi> for a normalized pure state."""
    value = np.vdot(state, operator @ state)

    if not np.isclose(value.imag, 0.0, atol=1e-10):
        raise ValueError(
            f"Expectation value has a non-negligible imaginary part: {value}"
        )

    return float(value.real)


def state_fidelity(
    state_a: ComplexArray,
    state_b: ComplexArray,
) -> float:
    """Calculate pure-state fidelity |<a|b>|^2."""
    overlap = np.vdot(state_a, state_b)
    return float(np.abs(overlap) ** 2)


def basis_probabilities(
    state: ComplexArray,
) -> NDArray[np.float64]:
    """Return probabilities in the ordered basis |00>, |01>, |10>, |11>."""
    probabilities = np.abs(state) ** 2

    if not np.isclose(np.sum(probabilities), 1.0, atol=1e-10):
        raise ValueError("State is not normalized.")

    return probabilities.real


def analytic_energy_spectrum(
    J: float,
    h: float,
) -> NDArray[np.float64]:
    """Return the analytical eigenvalues in ascending order."""
    omega = np.sqrt(J**2 + 4.0 * h**2)

    return np.sort(
        np.array(
            [-omega, -J, J, omega],
            dtype=float,
        )
    )
