# Digital Quantum Simulation of a Two-Qubit Ising Model

This repository develops and validates the real-time dynamics of a two-qubit transverse-field Ising model,

\[
H=-J\,Z_0Z_1-h\left(X_0+X_1\right),
\]

using both exact matrix evolution and gate-based Trotter approximations. The project was built as a compact, self-contained study of how a many-body Hamiltonian is translated from operator algebra into numerical evolution and then into a digital quantum circuit.

The calculations are deliberately developed in stages: first by hand, then with NumPy/SciPy, and finally with Qiskit. Analytical expressions and numerical results are cross-checked throughout with explicit assertions.

## Project scope

The repository covers:

- construction of one- and two-qubit basis states and Pauli operators;
- assembly and diagonalization of the two-qubit Ising Hamiltonian;
- exact real-time evolution from the initial state \(|00\rangle\);
- calculation of basis-state probabilities, magnetization, and spin correlation;
- first-order Lie-Trotter decomposition and its gate-level implementation;
- second-order symmetric Suzuki-Trotter decomposition;
- comparison of fidelity, observable errors, convergence order, and circuit cost.

## Notebooks

| Notebook | Content |
|---|---|
| [`01_exact_two_qubit_ising.ipynb`](01_exact_two_qubit_ising.ipynb) | Builds the Hamiltonian from tensor-product operators, verifies its spectrum, computes exact time evolution, and evaluates observables. |
| [`02_first_order_trotter.ipynb`](02_first_order_trotter.ipynb) | Derives the first-order Lie-Trotter step, maps the evolution to `RX` and `RZZ` gates, and validates the Qiskit statevector against a hand calculation. |
| [`03_second_order_trotter_convergence.ipynb`](03_second_order_trotter_convergence.ipynb) | Implements the symmetric second-order formula and compares first- and second-order convergence using state fidelity and observable errors. |

A typeset companion containing the analytical derivations is available here:

- [`docs/analytical_derivations.pdf`](docs/analytical_derivations.pdf)

## Main analytical results

Using the symmetric basis

\[
|\phi_\pm\rangle=\frac{|00\rangle\pm|11\rangle}{\sqrt{2}},
\qquad
|\psi_\pm\rangle=\frac{|01\rangle\pm|10\rangle}{\sqrt{2}},
\]

the Hamiltonian separates into two one-dimensional sectors and one two-dimensional symmetric sector. Defining

\[
\Omega=\sqrt{J^2+4h^2},
\]

the exact energy spectrum is

\[
E\in\{-\Omega,-J,J,\Omega\}.
\]

For the initial state \(|00\rangle\), the exact amplitudes are

\[
\begin{aligned}
a_{00}(t)&=\frac{1}{2}\left[e^{iJt}+\cos(\Omega t)+i\frac{J}{\Omega}\sin(\Omega t)\right],\\
a_{11}(t)&=\frac{1}{2}\left[-e^{iJt}+\cos(\Omega t)+i\frac{J}{\Omega}\sin(\Omega t)\right],\\
a_{01}(t)&=a_{10}(t)=i\frac{h}{\Omega}\sin(\Omega t).
\end{aligned}
\]

The first-order approximation is

\[
U_1(t;r)=\left[e^{-iH_{ZZ}t/r}e^{-iH_Xt/r}\right]^r,
\]

while the symmetric second-order approximation is

\[
U_2(t;r)=\left[e^{-iH_Xt/(2r)}e^{-iH_{ZZ}t/r}e^{-iH_Xt/(2r)}\right]^r.
\]

For fixed total time, their typical global operator/state errors scale as \(O(r^{-1})\) and \(O(r^{-2})\), respectively. In the small-error regime, the corresponding state infidelities commonly scale as \(O(r^{-2})\) and \(O(r^{-4})\).

## Shared helper modules

Reusable definitions are collected in [`Ising_sim_helper/`](Ising_sim_helper/):

- `operators.py`: basis states, Pauli matrices, tensor-product operators, and observables;
- `dynamics.py`: Hamiltonian construction, exact evolution, fidelity, probabilities, and expectation values;
- `circuits.py`: first- and second-order Qiskit Trotter circuits;
- `__init__.py`: selected public imports.

The notebooks retain the physical derivations and validation steps rather than hiding the calculation behind high-level library routines.

## Environment and execution

Python 3.10 or later is recommended. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy scipy matplotlib qiskit jupyterlab
jupyter lab
```

Start JupyterLab from the repository root so that the notebooks can import `Ising_sim_helper` directly.

Before committing changes, restart the kernel and run each notebook from top to bottom to ensure that no result depends on hidden notebook state.

## Validation strategy

The implementation uses several independent checks:

- operator actions are tested on every computational-basis vector;
- the constructed Hamiltonian is checked for Hermiticity;
- numerical eigenvalues are compared with the analytical spectrum;
- exact and analytical statevectors are compared component by component;
- hand-derived one-step Trotter states are compared with Qiskit statevectors;
- normalization, exchange symmetry, and limiting cases such as \(h=0\) and \(J=0\) are verified;
- convergence is studied using both state fidelity and observable errors.

## Limitations and possible extensions

The present repository uses an ideal statevector description of a two-qubit closed system. Natural extensions include finite-shot measurements, sampling uncertainty, noisy circuit simulation, hardware-aware transpilation, larger spin chains, and higher-order product formulas.

## License

This project is released under the [MIT License](LICENSE).


## Acknowledgements and use of AI tools

The analytical derivations, notebook implementation, numerical validation, and physical interpretation were carried out and checked by the author. OpenAI's ChatGPT was used as a learning and editorial aid, including discussion of intermediate derivations, debugging suggestions, review of code and documentation, and assistance with the organization and LaTeX typesetting of the companion PDF.
