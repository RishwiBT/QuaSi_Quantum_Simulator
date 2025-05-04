import requests

class APIClient:
    BASE_URL = "https://api.quasi.com"  # Replace with actual backend URL

    def __init__(self, api_key):
        self.api_key = api_key

    def submit_circuit(self, circuit_ir, shots=1024):
        """Submit circuit to backend"""
        response = requests.post(
            f"{self.BASE_URL}/submit",
            json={"circuit": circuit_ir, "shots": shots},
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        return response.json().get("job_id")

    def fetch_results(self, job_id):
        """Poll results from backend"""
        response = requests.get(
            f"{self.BASE_URL}/result/{job_id}",
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        return response.json()["result"]