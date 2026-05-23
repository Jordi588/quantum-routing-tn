import numpy as np
import quimb.tensor as qtn


def statevector_to_mps(statevector):

    n_qubits = int(
        np.log2(len(statevector))
    )

    mps = qtn.MatrixProductState.from_dense(
        statevector,
        dims=[2] * n_qubits
    )

    return mps