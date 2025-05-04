from qiskit import QuantumCircuit
from quasi.circuit_parser import CircuitParser  # ✅ CORRECT

# Initialize the circuit parser
parser = CircuitParser()

# Create a random Qiskit quantum circuit
qc = QuantumCircuit(3)  # 3 qubits
qc.h(0)
qc.cx(0, 1)
qc.rx(0.5, 2)
qc.measure_all()

# Convert to JSON (IR format)
circuit_ir = parser.convert_to_ir(qc)

# Print the result
import json
print(json.dumps(circuit_ir, indent=4))