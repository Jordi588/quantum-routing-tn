from fastapi import FastAPI

app = FastAPI(
    title="Quantum Routing TN"
)


@app.get("/")
def root():
    return {
        "message": "Quantum Routing Backend"
    }