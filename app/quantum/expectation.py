# from qiskit.quantum_info import Statevector


# def compute_expectation_value(
#     circuit,
#     hamiltonian
# ):

#     state = Statevector.from_instruction(
#         circuit
#     )

#     energy = state.expectation_value(
#         hamiltonian
#     )

#     return energy.real


from app.quantum.statevector import (
    get_statevector
)


def compute_expectation_value(
    circuit,
    hamiltonian
):

    state = get_statevector(circuit)

    energy = state.expectation_value(
        hamiltonian
    )

    return energy.real