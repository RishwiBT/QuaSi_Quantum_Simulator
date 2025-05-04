import time
import requests
from quasi.circuit_parser import CircuitParser

class QuantumSimulator:
    BASE_URL = "http://127.0.0.1:8000"  # Local API

    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.parser = CircuitParser()

    def run(self, circuit, shots=1024):
        """Submit a quantum circuit for simulation."""
        circuit_ir = self.parser.convert_to_ir(circuit)
        response = requests.post(f"{self.BASE_URL}/submit", json={"circuit": circuit_ir, "shots": shots})
        return response.json().get("job_id")

    def get_result(self, job_id):
        """Fetch results asynchronously with a single wait message."""
        print("Waiting for results...", end="", flush=True)  # Print only once
        while True:
            response = requests.get(f"{self.BASE_URL}/result/{job_id}")
            data = response.json()
            if data["status"] == "completed":
                print("\nResults received!")  # Print newline when done
                return data["result"]
            time.sleep(1)  # Reduce request frequency