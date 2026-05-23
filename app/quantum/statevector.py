from qiskit.quantum_info import Statevector


def get_statevector(circuit):

    state = Statevector.from_instruction(
        circuit
    )

    return state