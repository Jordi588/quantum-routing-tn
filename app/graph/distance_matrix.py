import numpy as np


def build_distance_matrix(G):

    nodes = sorted(G.nodes())

    n = len(nodes)

    D = np.zeros((n, n))

    for i in nodes:
        for j in nodes:

            if i == j:
                continue

            D[i][j] = G[i][j]["weight"]

    return D