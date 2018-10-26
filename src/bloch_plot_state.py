import numpy as np

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.tools.visualization import plot_state, plot_histogram

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.s(q).inverse()
qc.h(q)
qc.rz(np.pi/4, q)
qc.rx(-np.pi/4, q)
qc.barrier()

backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()

data = np.round(result.get_data(qc)['statevector'], 5)
print(data)
plot_state(data, 'city')
plot_state(data, 'bloch')
plot_state(data, 'qsphere')
plot_state(data, 'paulivec')