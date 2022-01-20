from benchmarks import pi_benchmark
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World"}


@app.get("/py_benchmark/{num_samples}/{num_repeats}")
def get_py_benchmark(num_samples: int, num_repeats: int):
    return pi_benchmark(num_samples, num_repeats)