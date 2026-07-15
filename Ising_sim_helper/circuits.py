"""Qiskit circuits for first- and second-order Trotter evolution."""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

import numpy as np
from numpy.typing import NDArray


ComplexArray = NDArray[np.complex128]


def first_order_trotter_circuit(
    time: float,
    J: float,
    h: float,
    n_steps: int,
) -> QuantumCircuit:
    """Construct a first-order Lie-Trotter circuit."""
    if n_steps < 1:
        raise ValueError("n_steps must be at least 1")

    dt = time / n_steps

    theta_x = -2.0 * h * dt
    theta_zz = -2.0 * J * dt

    circuit = QuantumCircuit(2)

    for _ in range(n_steps):
        circuit.rx(theta_x, 0)
        circuit.rx(theta_x, 1)
        circuit.rzz(theta_zz, 0, 1)

    return circuit


def second_order_trotter_circuit(
    time: float,
    J: float,
    h: float,
    n_steps: int,
) -> QuantumCircuit:
    """Construct a symmetric second-order Suzuki-Trotter circuit."""
    if n_steps < 1:
        raise ValueError("n_steps must be at least 1")

    dt = time / n_steps

    theta_x_half = -h * dt
    theta_zz = -2.0 * J * dt

    circuit = QuantumCircuit(2)

    for _ in range(n_steps):
        circuit.rx(theta_x_half, 0)
        circuit.rx(theta_x_half, 1)

        circuit.rzz(theta_zz, 0, 1)

        circuit.rx(theta_x_half, 0)
        circuit.rx(theta_x_half, 1)

    return circuit


def statevector_from_circuit(
    circuit: QuantumCircuit,
) -> ComplexArray:
    """Return the statevector produced from the Qiskit |00> state."""
    return np.asarray(
        Statevector.from_instruction(circuit).data,
        dtype=complex,
    )
