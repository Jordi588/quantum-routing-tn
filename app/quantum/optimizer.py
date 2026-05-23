import numpy as np

from scipy.optimize import minimize

from app.quantum.expectation import (
    compute_expectation_value
)


def optimize_qaoa(
    qaoa_circuit,
    hamiltonian
):

    params = list(
        qaoa_circuit.parameters
    )

    def objective(x):

        bound = qaoa_circuit.assign_parameters({
            params[0]: x[0],
            params[1]: x[1]
        })

        return compute_expectation_value(
            bound,
            hamiltonian
        )

    x0 = np.random.rand(2)

    result = minimize(
        objective,
        x0,
        method="COBYLA"
    )

    return result