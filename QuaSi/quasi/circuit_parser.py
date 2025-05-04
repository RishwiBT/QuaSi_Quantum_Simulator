from qiskit import QuantumCircuit
import cirq

class CircuitParser:
    """Parses quantum circuits from Qiskit and Cirq into IR format."""

    def convert_to_ir(self, circuit):
        if isinstance(circuit, QuantumCircuit):
            return self._parse_qiskit(circuit)
        elif isinstance(circuit, cirq.Circuit):
            return self._parse_cirq(circuit)
        else:
            raise ValueError("Unsupported circuit format")

    def _parse_qiskit(self, circuit):
        """Convert Qiskit circuit to IR format."""
        ir = {"qubits": circuit.num_qubits, "gates": []}
        
        for instruction in circuit.data:
            gate_name = instruction.operation.name.upper()
            qubits = [q._index for q in instruction.qubits]

            # Extract parameters if they exist
            params = instruction.operation.params
            gate_data = {"name": gate_name, "qubits": qubits}

            if params:  # Only add params if they exist
                gate_data["params"] = params

            # Exclude barriers if not needed
            if gate_name != "BARRIER":
                ir["gates"].append(gate_data)

        return ir

    def _parse_cirq(self, circuit):
        """Convert Cirq circuit to IR format."""
        ir = {"qubits": len(circuit.all_qubits()), "gates": []}

        for op in circuit:
            gate_name = str(op.gate).upper()
            qubits = [q.x for q in op.qubits]  # Extract qubit indices

            gate_data = {"name": gate_name, "qubits": qubits}

            # Extract parameters if they exist
            if hasattr(op.gate, 'exponent'):
                gate_data["params"] = [op.gate.exponent]

            ir["gates"].append(gate_data)

        return ir