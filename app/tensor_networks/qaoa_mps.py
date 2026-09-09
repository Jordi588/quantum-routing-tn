import quimb as qu
import quimb.tensor as qtn
import numpy as np


def create_initial_mps(n_qubits):

    psi = qtn.MPS_computational_state(
        "0" * n_qubits
    )

    # Prepare |+>^n
    H = qu.hadamard()

    for i in range(n_qubits):
        psi.gate_(
            H,
            i
        )

    return psi


def apply_cost_layer(
    psi,
    graph,
    gamma
):

    Z = qu.pauli("Z")
    ZZ = np.kron(Z, Z)

    for i, j, data in graph.edges(data=True):

        weight = float(data.get("weight", 1.0))

        # U_ij = exp(-i * gamma * weight * Z_i Z_j)
        U = qu.expm(
            -1j * gamma * weight * ZZ
        )

        # Two-qubit gate
        # swap+split handles non-neighboring qubits
        psi.gate_(
            U,
            (i, j),
            contract="swap+split"
        )

    return psi


def apply_mixer_layer(
    psi,
    beta
):

    rx = qu.rx(2 * beta)

    for i in range(psi.nsites):

        psi.gate_(
            rx,
            i
        )

    return psi


def run_qaoa_mps(
    graph,
    depth,
    gamma,
    beta
):

    n_qubits = graph.number_of_nodes()

    psi = create_initial_mps(
        n_qubits
    )

    for _ in range(depth):

        psi = apply_cost_layer(
            psi,
            graph,
            gamma
        )

        psi = apply_mixer_layer(
            psi,
            beta
        )

    return psi