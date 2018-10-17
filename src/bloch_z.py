from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.tools.visualization import plot_bloch_vector

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)


# Build the circuit
def build_circuit(state=None):
    qc = QuantumCircuit(q, c)
    if state == None:
        state = [1, 0]
    qc.initialize(state, q)
    qc.barrier()
    return qc


# Execute the circuit
def execute_circuit(qc):
    backend = Aer.get_backend('qasm_simulator_py')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    return result


# Plot Bloch sphere
def plot_bloch(qc):
    qc.measure(q, c)
    result = execute_circuit(qc)
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
    plot_bloch_vector([0, 0, (p0 - p1)])


if __name__ == "__main__":
    qc = build_circuit()
    plot_bloch(qc)
    qc = build_circuit()
    qc.z(q)
    plot_bloch(qc)

    qc = build_circuit([0, 1])
    plot_bloch(qc)
    qc = build_circuit([0, 1])
    qc.z(q)
    plot_bloch(qc)
