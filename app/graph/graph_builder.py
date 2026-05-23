import networkx as nx
import numpy as np


def euclidean_distance(x1, y1, x2, y2):

    return np.sqrt(
        (x1 - x2)**2 +
        (y1 - y2)**2
    )


def build_graph(df):

    G = nx.Graph()

    # Add nodes
    for _, row in df.iterrows():

        G.add_node(
            int(row["id"]),
            pos=(row["x"], row["y"]),
            demand=row["demand"]
        )

    # Add weighted edges
    nodes = list(G.nodes())

    for i in nodes:
        for j in nodes:

            if i >= j:
                continue

            xi, yi = G.nodes[i]["pos"]
            xj, yj = G.nodes[j]["pos"]

            dist = euclidean_distance(
                xi, yi,
                xj, yj
            )

            G.add_edge(
                i,
                j,
                weight=dist
            )

    return G