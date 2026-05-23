import quimb as qu
import quimb.tensor as qtn


def create_initial_mps(
    n_qubits
):

    psi = qtn.MPS_computational_state(
        "0" * n_qubits
    )

    # Apply Hadamards
    for i in range(n_qubits):

        psi.gate_(
            qu.hadamard(),
            i
        )

    return psi


# def apply_cost_layer(
#     psi,
#     graph,
#     gamma
# ):

#     for i, j in graph.edges():

#         weight = graph[i][j]["weight"]

#         zz_gate = qu.ham_heis(
#             1.0,
#             j=(0, 0, weight)
#         )

#         U = qu.expm(
#             -1j * gamma * zz_gate
#         )

#         psi.gate_(
#             U,
#             (i, j),
#             contract="swap+split"
#         )

#     return psi


import quimb as qu
import numpy as np


# def apply_cost_layer(
#     psi,
#     graph,
#     gamma
# ):

#     # Pauli Z
#     Z = qu.pauli('Z')

#     # ZZ interaction
#     ZZ = np.kron(Z, Z)

#     for i, j in graph.edges():

#         weight = graph[i][j]["weight"]

#         # U = exp(-i gamma w ZZ)
#         U = qu.expm(
#             -1j * gamma * weight * ZZ
#         )

#         psi.gate_(
#             U,
#             (i, j),
#             contract="swap+split"
#         )

#     return psi


import quimb as qu
import numpy as np


def apply_cost_layer(
    psi,
    graph,
    gamma
):

    Z = qu.pauli('Z')

    ZZ = np.kron(Z, Z)

    for i, j in graph.edges():

        weight = graph[i][j]["weight"]

        # 4x4 unitary
        U = qu.expm(
            -1j * gamma * weight * ZZ
        )

        # reshape into rank-4 tensor
        U = U.reshape(2, 2, 2, 2)

        psi.gate_(
            U,
            (i, j),
            contract='swap+split'
        )

    return psi


# def apply_mixer_layer(
#     psi,
#     beta
# ):

#     for i in range(psi.nsites):

#         rx = qu.rx(2 * beta)

#         psi.gate_(
#             rx,
#             i
#         )

#     return psi


def apply_mixer_layer(
    psi,
    beta
):

    for i in range(psi.nsites):

        rx = qu.rx(2 * beta)

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

    n_qubits = len(graph.nodes())

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