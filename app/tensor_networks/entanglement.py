import numpy as np


def entanglement_entropy(
    singular_values
):

    probs = singular_values**2

    probs = probs[
        probs > 1e-12
    ]

    entropy = -np.sum(
        probs * np.log(probs)
    )

    return entropy