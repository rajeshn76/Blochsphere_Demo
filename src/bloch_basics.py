import math

from qiskit.tools.visualization import plot_bloch_vector


# Plot Bloch sphere
def plot_bloch(ϴ=0, ϕ=0, r=1):
    x = r * math.sin(ϴ) * math.cos(ϕ)
    y = r * math.sin(ϴ) * math.sin(ϕ)
    z = r * math.cos(ϴ)
    print("{ϴ = %s, ϕ = %s, r = %s}" % (ϴ, ϕ, r))

    plot_bloch_vector([x, y, z])


if __name__ == "__main__":
    plot_bloch()
    plot_bloch(math.pi / 4)
    plot_bloch(math.pi / 2)
    plot_bloch(3 * math.pi / 4)

    plot_bloch(math.pi)
    plot_bloch(math.pi, 2 * math.pi)

    plot_bloch(math.pi / 2, 3 * math.pi / 2)
    plot_bloch(math.pi / 2, math.pi / 2)
