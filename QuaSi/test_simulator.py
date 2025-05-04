from quasi.simulator import StateVectorSimulator

sim = StateVectorSimulator(2)
sim.apply_gate('h', [0])
sim.apply_gate('cx', [0, 1])
print("Probabilities:", sim.get_probabilities())  # Expect: {'11': 1.0}