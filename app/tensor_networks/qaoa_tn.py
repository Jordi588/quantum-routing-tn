import quimb.tensor as qtn


def build_qaoa_tensor_network(
    n_qubits
):

    circuit = qtn.Circuit(
        n_qubits
    )

    return circuit