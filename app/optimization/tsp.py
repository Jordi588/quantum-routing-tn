def create_binary_variables(n):

    variables = []

    for city in range(n):
        for time in range(n):

            variables.append(
                (city, time)
            )

    return variables