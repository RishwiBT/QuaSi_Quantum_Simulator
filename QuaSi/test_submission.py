from qiskit import QuantumCircuit
from quasi.client import QuantumSimulator

# Initialize the simulator
sim = QuantumSimulator()

# Create a test circuit
qc = QuantumCircuit(2)
qc.x(0)
qc.cx(0, 1)
qc.measure_all()

# Submit the circuit
job_id = sim.run(qc)
print(f"Job ID: {job_id}")

# Fetch the result
result = sim.get_result(job_id)
print(f"Result: {result}")