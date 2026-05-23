from qiskit.circuit.library import QAOAAnsatz


def build_qaoa_circuit(ising_operator, reps=1):

    circuit = QAOAAnsatz(
        cost_operator=ising_operator,
        reps=reps
    )

    return circuit