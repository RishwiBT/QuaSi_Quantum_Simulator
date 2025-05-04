import quimb as qu
import quimb.tensor as qtn
import numpy as np

def simulate_circuit(circuit_json, shots=1024):
    """Simulate a quantum circuit using Tensor Networks."""
    num_qubits = circuit_json["qubits"]
    tn = qtn.Circuit(num_qubits)

    # Apply Gates
    for gate in circuit_json["gates"]:
        gate_name = gate["name"]
        qubits = gate["qubits"]

        if gate_name == "H":
            for q in qubits:
                tn.apply_gate("H", q)

        elif gate_name == "X":
            for q in qubits:
                tn.apply_gate("X", q)

        elif gate_name == "Y":
            for q in qubits:
                tn.apply_gate("Y", q)

        elif gate_name == "Z":
            for q in qubits:
                tn.apply_gate("Z", q)

        elif gate_name == "CX":  # CNOT
            tn.apply_gate("CX", *qubits)

        elif gate_name == "CY":
            tn.apply_gate("CY", *qubits)

        elif gate_name == "CZ":
            tn.apply_gate("CZ", *qubits)

        elif gate_name == "SWAP":
            tn.apply_gate("SWAP", *qubits)

        elif gate_name == "TOFFOLI":
            tn.apply_gate("CCX", *qubits)  # CCX is Toffoli gate

        elif gate_name in ["RX", "RY", "RZ"]:
            for q in qubits:
                tn.apply_gate(gate_name, q, param=gate.get("params", [0])[0])

    # Simulate measurement outcomes
    results = tn.sample(shots)
    probabilities = {k: v / shots for k, v in results.items()}
    
    return probabilities