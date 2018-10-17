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

meas_x = QuantumCircuit(q, c)
meas_x.barrier()
meas_x.h(q)
meas_x.measure(q, c)

meas_y = QuantumCircuit(q, c)
meas_y.barrier()
meas_y.s(q).inverse()
meas_y.h(q)
meas_y.measure(q, c)

meas_z = QuantumCircuit(q, c)
meas_z.barrier()
meas_z.measure(q, c)

bloch_vector = ['x', 'y', 'z']
circuits = []

middle = QuantumCircuit(q, c)
middle.h(q)

#apply the single-qubit quantum gate: Z|1>
middle.x(q)
middle.z(q)

circuits.append(pre + middle + meas_x)
circuits.append(pre + middle + meas_y)
circuits.append(pre + middle + meas_z)

# Execute the circuit
backend = Aer.get_backend('qasm_simulator_py')
job = execute(circuits, backend, shots=1024)
result = job.result()

# Plot the result
bloch = [0, 0, 0]
for bloch_index in range(len(bloch_vector)):
    qc = circuits[bloch_index]
    plot_circuit(qc)
    data = result.get_counts(qc)
    try:
        p0 = data['0'] / 1024.0
    except KeyError:
        p0 = 0
    try:
        p1 = data['1'] / 1024.0
    except KeyError:
        p1 = 0
    bloch[bloch_index] = p0 - p1
print("Z|1> = -|1>")
plot_bloch_vector(bloch)

