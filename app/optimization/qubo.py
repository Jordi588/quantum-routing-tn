from qiskit_optimization import QuadraticProgram


def build_tsp_qubo(distance_matrix):

    n = len(distance_matrix)

    qp = QuadraticProgram()

    # --------------------------------
    # Binary variables
    # --------------------------------

    for i in range(n):
        for t in range(n):

            qp.binary_var(
                name=f"x_{i}_{t}"
            )

    # --------------------------------
    # Constraint:
    # each city exactly once
    # --------------------------------

    for i in range(n):

        qp.linear_constraint(
            linear={
                f"x_{i}_{t}": 1
                for t in range(n)
            },
            sense="==",
            rhs=1,
            name=f"city_{i}"
        )

    # --------------------------------
    # Constraint:
    # one city per time step
    # --------------------------------

    for t in range(n):

        qp.linear_constraint(
            linear={
                f"x_{i}_{t}": 1
                for i in range(n)
            },
            sense="==",
            rhs=1,
            name=f"time_{t}"
        )

    # --------------------------------
    # Objective function
    # --------------------------------

    quadratic_objective = {}

    for i in range(n):
        for j in range(n):

            if i == j:
                continue

            for t in range(n):

                next_t = (t + 1) % n

                quadratic_objective[
                    (
                        f"x_{i}_{t}",
                        f"x_{j}_{next_t}"
                    )
                ] = distance_matrix[i][j]

    qp.minimize(
        quadratic=quadratic_objective
    )

    return qp