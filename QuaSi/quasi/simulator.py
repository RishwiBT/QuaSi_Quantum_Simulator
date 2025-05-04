import numpy as np

class StateVectorSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2 ** num_qubits, dtype=complex)
        self.state[0] = 1.0  # Initial state |00...0⟩

        # Gate definitions
        self.gates = {
            'x': np.array([[0, 1], [1, 0]], dtype=complex),
            'h': 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype=complex),
            'cx': np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]
            ], dtype=complex)
        }

    def apply_gate(self, gate_name, qubits):
        if gate_name == 'cx':
            self._apply_cx(*qubits)
        else:
            self._apply_single_qubit_gate(self.gates[gate_name], qubits[0])

    def _apply_single_qubit_gate(self, gate_matrix, target_qubit):
        """Apply a single-qubit gate to the full statevector."""
        I = np.eye(2, dtype=complex)
        ops = [I] * self.num_qubits

        # Qiskit uses little-endian: qubit 0 = LSB = rightmost in tensor product
        ops[self.num_qubits - 1 - target_qubit] = gate_matrix

        full_gate = ops[0]
        for op in ops[1:]:
            full_gate = np.kron(full_gate, op)

        self.state = full_gate @ self.state

    def _apply_cx(self, control_qubit, target_qubit):
        """Apply a controlled-X (CNOT) gate correctly using Qiskit-style bit order."""
        new_state = np.zeros_like(self.state)

        for i in range(len(self.state)):
            # Check control qubit bit (Qiskit convention: qubit 0 is LSB)
            if (i >> control_qubit) & 1:
                # Flip the target qubit bit
                flipped = i ^ (1 << target_qubit)
                new_state[flipped] += self.state[i]
            else:
                new_state[i] += self.state[i]

        self.state = new_state

    def get_probabilities(self):
        """Returns probabilities for each basis state."""
        probs = np.abs(self.state) ** 2
        result = {}
        for i, p in enumerate(probs):
            if p > 1e-6:
                result[format(i, f'0{self.num_qubits}b')] = round(p, 6)
        return result