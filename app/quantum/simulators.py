from qiskit_aer import AerSimulator
from qiskit import transpile


def run_statevector(circuit):

    simulator = AerSimulator()

    compiled = transpile(
        circuit,
        simulator
    )

    result = simulator.run(
        compiled
    ).result()

    return result