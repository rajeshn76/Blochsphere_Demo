# quantum_phase_bloch.py
import numpy as np

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.tools.visualization import plot_bloch_vector, plot_circuit

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuits
pre = QuantumCircuit(q, c)
pre.h(q)
pre.barrier()

meas_z = QuantumCircuit(q, c)
meas_z.barrier()
meas_z.h(q)
meas_z.measure(q, c)

exp_vector = range(0, 3)
circuits = []
for exp_index in exp_vector:
    middle = QuantumCircuit(q, c)
    phase = 2 * np.pi * exp_index / (len(exp_vector) - 1)
    middle.rz(phase, q)
    circuits.append(pre + middle + meas_z)

# Execute the circuit
backend = Aer.get_backend('qasm_simulator_py')
job = execute(circuits, backend, shots=1024)
result = job.result()

# Plot the result
for exp_index in exp_vector:
    bloch = [0, 0, 0]
    qc = circuits[exp_index]
    plot_circuit(qc)
    data = result.get_counts(qc)
    try:
        p0 = data['0'] / 1024.0
    except KeyError:
        p0 = 0.0
    try:
        p1 = data['1'] / 1024.0
    except KeyError:
        p1 = 0.0
    print("Probabilities: {'0' : %s, '1' : %s}" % (p0, p1))
    bloch[2] = (p0 - p1)
    print("bloch vector (for phase : %s) :: %s" % (2 * np.pi * exp_index / (len(exp_vector) - 1) , bloch))
    plot_bloch_vector(bloch)

