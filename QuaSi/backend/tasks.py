import asyncio
import random
from database import JOBS
from gpu_simulator import simulate_circuit

async def process_circuit(job_id, circuit, shots):
    """Execute the quantum circuit using the GPU simulator."""
    await asyncio.sleep(random.uniform(1, 3))  # Simulate processing delay

    result = simulate_circuit(circuit, shots)  # Call GPU-based simulator

    JOBS[job_id] = {"status": "completed", "result": {"probabilities": result}}