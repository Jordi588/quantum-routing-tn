import pandas as pd


def load_solomon(path: str) -> pd.DataFrame:
    """
    Load Solomon VRPTW dataset.
    """

    customers = []

    with open(path, "r") as f:
        lines = f.readlines()

    # Solomon data starts around line 9
    for line in lines[9:]:

        parts = line.split()

        if len(parts) < 7:
            continue

        customers.append({
            "id": int(parts[0]),
            "x": float(parts[1]),
            "y": float(parts[2]),
            "demand": float(parts[3]),
            "ready_time": float(parts[4]),
            "due_date": float(parts[5]),
            "service_time": float(parts[6]),
        })

    return pd.DataFrame(customers)