---
name: physics
description: '**KNOWLEDGE SKILL** — Explain, derive, compute, and simulate physics concepts across classical mechanics, electromagnetism, thermodynamics, quantum mechanics, relativity, optics, waves, fluid dynamics, and modern physics. USE FOR: physics problem solving, derivations, dimensional analysis, unit conversions, numerical simulations, physics engine concepts, exam preparation, and conceptual explanations. DO NOT USE FOR: pure mathematics without physics context (use a math skill), chemistry-only topics, or engineering design without physics analysis. INVOKES: file system tools for scripts and notes, terminal for numerical computation and simulation code.'
---

# Physics Skill

## Overview

This skill provides comprehensive support for physics problem solving, conceptual explanation, derivation, numerical computation, and simulation across all major branches of physics. It covers classical mechanics, electromagnetism, thermodynamics and statistical mechanics, quantum mechanics, special and general relativity, optics, waves and oscillations, fluid dynamics, nuclear and particle physics, and astrophysics.

## Key Capabilities

### Classical Mechanics

- Kinematics: displacement, velocity, acceleration, projectile motion, circular motion
- Newton's laws of motion, free-body diagrams, friction, tension, normal forces
- Work, energy, power, and the work-energy theorem
- Conservation of energy, momentum, and angular momentum
- Rotational dynamics: torque, moment of inertia, angular momentum, rolling motion
- Gravitational fields, orbits, Kepler's laws, escape velocity
- Oscillations: simple harmonic motion, damped and driven oscillators, resonance
- Lagrangian and Hamiltonian mechanics, generalized coordinates, variational principles

### Electromagnetism

- Coulomb's law, electric fields, Gauss's law, electric potential
- Capacitance, dielectrics, energy stored in electric fields
- Current, resistance, Ohm's law, Kirchhoff's laws, RC/RL/RLC circuits
- Magnetic fields, Biot-Savart law, Ampère's law, Lorentz force
- Faraday's law, Lenz's law, electromagnetic induction, inductance
- Maxwell's equations in differential and integral form
- Electromagnetic waves, Poynting vector, radiation pressure
- AC circuits, impedance, resonance, power factor

### Thermodynamics and Statistical Mechanics

- Temperature, heat, internal energy, specific heat, calorimetry
- Laws of thermodynamics (zeroth through third)
- Ideal gas law, kinetic theory, Maxwell-Boltzmann distribution
- Heat engines, Carnot cycle, entropy, free energy
- Phase transitions, latent heat, Clausius-Clapeyron equation
- Statistical ensembles: microcanonical, canonical, grand canonical
- Partition functions, Boltzmann distribution, Fermi-Dirac and Bose-Einstein statistics
- Blackbody radiation, Stefan-Boltzmann law, Wien's displacement law

### Quantum Mechanics

- Wave-particle duality, de Broglie wavelength, uncertainty principle
- Schrödinger equation (time-dependent and time-independent)
- Infinite and finite potential wells, quantum tunneling, harmonic oscillator
- Hydrogen atom, orbital angular momentum, spin, magnetic quantum numbers
- Operators, eigenvalues, expectation values, commutation relations
- Dirac notation, matrix mechanics, measurement postulates
- Perturbation theory, variational method, WKB approximation
- Entanglement, Bell's theorem, quantum information basics

### Special and General Relativity

- Lorentz transformations, time dilation, length contraction
- Relativistic momentum, energy, mass-energy equivalence (E = mc²)
- Spacetime diagrams, Minkowski metric, four-vectors
- Twin paradox, relativistic Doppler effect
- Equivalence principle, curved spacetime, geodesics
- Schwarzschild metric, gravitational redshift, black holes
- Gravitational lensing, gravitational waves (conceptual)
- Cosmological models: Friedmann equations, Hubble's law, expanding universe

### Waves and Optics

- Wave equation, superposition, interference, diffraction
- Standing waves, harmonics, resonance in strings and pipes
- Sound waves, Doppler effect, intensity, decibels
- Reflection, refraction, Snell's law, total internal reflection
- Thin lenses and mirrors, ray diagrams, lens/mirror equations
- Wave optics: Young's double slit, single slit diffraction, diffraction gratings
- Polarization, Brewster's angle, Malus's law
- Optical instruments: microscope, telescope, camera, fiber optics

### Fluid Dynamics

- Fluid statics: pressure, Pascal's law, Archimedes' principle, buoyancy
- Continuity equation, Bernoulli's equation, Venturi effect
- Viscosity, Poiseuille's law, Reynolds number, laminar vs turbulent flow
- Navier-Stokes equations (conceptual and simplified cases)
- Surface tension, capillarity, droplets

### Nuclear and Particle Physics

- Atomic structure, isotopes, nuclear binding energy, mass defect
- Radioactive decay: alpha, beta, gamma; half-life, decay chains
- Nuclear fission and fusion, Q-value, cross sections
- Standard Model: quarks, leptons, bosons, fundamental interactions
- Conservation laws: charge, baryon number, lepton number, strangeness
- Feynman diagrams (basic interpretation)

### Astrophysics and Cosmology

- Stellar structure, Hertzsprung-Russell diagram, stellar evolution
- Nucleosynthesis, main sequence, white dwarfs, neutron stars, black holes
- Hubble's law, redshift, cosmic microwave background
- Dark matter and dark energy (conceptual overview)
- Big Bang model, cosmic inflation (qualitative)

## Usage Examples

### Solve a Mechanics Problem

```
A 5 kg block slides down a 30° incline with coefficient
of kinetic friction 0.2. Find the acceleration and the
speed after traveling 4 meters from rest.
```

### Derive an Equation

```
Derive the time period of a simple pendulum
using the small-angle approximation from Newton's second law.
```

### Quantum Mechanics Calculation

```
Find the energy levels and wavefunctions for a particle
in a one-dimensional infinite potential well of width L.
Calculate the probability of finding the particle
in the left third of the well for the ground state.
```

### Electromagnetism Analysis

```
A parallel-plate capacitor with plate area A and separation d
is filled with a dielectric of constant κ. Derive the capacitance
and calculate the energy stored when charged to voltage V.
```

### Numerical Simulation

```
Write a Python simulation of a double pendulum
showing chaotic motion with animated visualization.
```

### Dimensional Analysis

```
Use dimensional analysis to derive the dependence
of the period of a simple pendulum on length and
gravitational acceleration.
```

## Common Patterns

### Problem-Solving Framework

```
1. IDENTIFY: Read the problem; list knowns and unknowns
2. DIAGRAM: Draw a picture, free-body diagram, or circuit diagram
3. MODEL: Choose the physical model and applicable laws
4. EQUATIONS: Write the governing equations
5. SOLVE: Solve algebraically first, then substitute numbers
6. CHECK: Verify units, limiting cases, and reasonableness
```

### Key Equations — Classical Mechanics

```
Kinematics (constant acceleration):
  v = v₀ + at
  x = x₀ + v₀t + ½at²
  v² = v₀² + 2a(x - x₀)

Newton's Second Law:
  ΣF = ma       (translational)
  Στ = Iα       (rotational)

Work-Energy Theorem:
  W_net = ΔKE = ½mv² - ½mv₀²

Conservation of Energy:
  KE₁ + PE₁ + W_nc = KE₂ + PE₂

Conservation of Momentum:
  Σp_before = Σp_after    (if ΣF_ext = 0)

Gravitational Force:
  F = GMm/r²

Simple Harmonic Motion:
  x(t) = A cos(ωt + φ)
  ω = √(k/m)     (spring)
  ω = √(g/L)     (pendulum, small angle)
  T = 2π/ω
```

### Key Equations — Electromagnetism

```
Coulomb's Law:
  F = kq₁q₂/r²     (k = 1/4πε₀ ≈ 8.99 × 10⁹ N·m²/C²)

Electric Field and Potential:
  E = F/q = kQ/r²
  V = kQ/r
  E = -dV/dr

Gauss's Law:
  ∮ E · dA = Q_enc / ε₀

Capacitance:
  C = Q/V = ε₀A/d     (parallel plate)
  U = ½CV² = ½Q²/C

Ohm's Law:
  V = IR
  P = IV = I²R = V²/R

Kirchhoff's Laws:
  Junction: ΣI_in = ΣI_out
  Loop:     ΣV = 0

Magnetic Force:
  F = qv × B          (on charge)
  F = IL × B          (on wire)

Faraday's Law:
  EMF = -dΦ_B/dt

Maxwell's Equations (integral form):
  ∮ E · dA = Q/ε₀                    (Gauss)
  ∮ B · dA = 0                       (no monopoles)
  ∮ E · dl = -dΦ_B/dt                (Faraday)
  ∮ B · dl = μ₀I + μ₀ε₀ dΦ_E/dt     (Ampère-Maxwell)
```

### Key Equations — Thermodynamics

```
Ideal Gas Law:
  PV = nRT = NkT

First Law:
  ΔU = Q - W

Entropy:
  ΔS = Q_rev / T
  S = k_B ln Ω

Carnot Efficiency:
  η = 1 - T_cold / T_hot

Heat Transfer:
  Conduction:  P = kA(ΔT)/L
  Radiation:   P = εσAT⁴
  Stefan-Boltzmann: σ = 5.67 × 10⁻⁸ W/(m²·K⁴)
```

### Key Equations — Quantum Mechanics

```
de Broglie Wavelength:
  λ = h/p = h/(mv)

Heisenberg Uncertainty:
  Δx · Δp ≥ ℏ/2
  ΔE · Δt ≥ ℏ/2

Schrödinger Equation (time-independent):
  -ℏ²/(2m) d²ψ/dx² + V(x)ψ = Eψ

Infinite Well Energy Levels:
  Eₙ = n²π²ℏ² / (2mL²)     n = 1, 2, 3, ...

Hydrogen Atom:
  Eₙ = -13.6 eV / n²

Photon Energy:
  E = hf = hc/λ

Photoelectric Effect:
  KE_max = hf - φ       (φ = work function)
```

### Key Equations — Special Relativity

```
Lorentz Factor:
  γ = 1 / √(1 - v²/c²)

Time Dilation:
  Δt = γΔt₀

Length Contraction:
  L = L₀/γ

Relativistic Momentum:
  p = γmv

Energy-Momentum Relation:
  E² = (pc)² + (mc²)²
  E = γmc²

Mass-Energy Equivalence:
  E₀ = mc²
```

### Key Equations — Waves and Optics

```
Wave Equation:
  v = fλ

Standing Waves:
  String fixed both ends: λₙ = 2L/n,  fₙ = nv/(2L)
  Open pipe:              λₙ = 2L/n,  fₙ = nv/(2L)
  Closed pipe:            λₙ = 4L/n,  fₙ = nv/(4L)  (odd n)

Doppler Effect:
  f' = f (v ± v_observer) / (v ∓ v_source)

Snell's Law:
  n₁ sin θ₁ = n₂ sin θ₂

Thin Lens Equation:
  1/f = 1/d_o + 1/d_i

Double Slit (maxima):
  d sin θ = mλ       m = 0, ±1, ±2, ...

Single Slit (minima):
  a sin θ = mλ       m = ±1, ±2, ...

Diffraction Grating (maxima):
  d sin θ = mλ
```

### Python — Numerical Simulation (Projectile Motion)

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
v0 = 50        # m/s initial speed
theta = 45     # degrees launch angle
g = 9.81       # m/s² gravitational acceleration
dt = 0.01      # time step

# Initial conditions
theta_rad = np.radians(theta)
vx, vy = v0 * np.cos(theta_rad), v0 * np.sin(theta_rad)
x, y = 0.0, 0.0

xs, ys = [x], [y]

# Euler integration
while y >= 0:
    vy -= g * dt
    x += vx * dt
    y += vy * dt
    xs.append(x)
    ys.append(y)

plt.figure(figsize=(10, 5))
plt.plot(xs, ys, 'b-', linewidth=2)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Height (m)')
plt.title(f'Projectile Motion (v₀={v0} m/s, θ={theta}°)')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.tight_layout()
plt.savefig('projectile.png', dpi=150)
plt.show()

# Analytical comparison
R = v0**2 * np.sin(2 * theta_rad) / g
H = v0**2 * np.sin(theta_rad)**2 / (2 * g)
T = 2 * v0 * np.sin(theta_rad) / g
print(f"Range: {R:.2f} m, Max Height: {H:.2f} m, Time of Flight: {T:.2f} s")
```

### Python — Double Pendulum Simulation

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def double_pendulum(t, state, L1, L2, m1, m2, g):
    θ1, ω1, θ2, ω2 = state
    Δθ = θ2 - θ1

    denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(Δθ)**2
    denom2 = (L2 / L1) * denom1

    dω1 = (m2 * L1 * ω1**2 * np.sin(Δθ) * np.cos(Δθ)
          + m2 * g * np.sin(θ2) * np.cos(Δθ)
          + m2 * L2 * ω2**2 * np.sin(Δθ)
          - (m1 + m2) * g * np.sin(θ1)) / denom1

    dω2 = (-m2 * L2 * ω2**2 * np.sin(Δθ) * np.cos(Δθ)
          + (m1 + m2) * g * np.sin(θ1) * np.cos(Δθ)
          - (m1 + m2) * L1 * ω1**2 * np.sin(Δθ)
          - (m1 + m2) * g * np.sin(θ2)) / denom2

    return [ω1, dω1, ω2, dω2]

# Parameters
L1, L2 = 1.0, 1.0
m1, m2 = 1.0, 1.0
g = 9.81
θ1_0, θ2_0 = np.radians(120), np.radians(150)

t_span = (0, 20)
t_eval = np.linspace(*t_span, 2000)

sol = solve_ivp(double_pendulum, t_span, [θ1_0, 0, θ2_0, 0],
                t_eval=t_eval, args=(L1, L2, m1, m2, g),
                method='RK45', rtol=1e-10)

θ1, θ2 = sol.y[0], sol.y[2]
x1 =  L1 * np.sin(θ1)
y1 = -L1 * np.cos(θ1)
x2 = x1 + L2 * np.sin(θ2)
y2 = y1 - L2 * np.cos(θ2)

# Plot trajectory
plt.figure(figsize=(8, 8))
plt.plot(x2, y2, 'r-', alpha=0.3, linewidth=0.5)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Double Pendulum — Chaotic Trajectory')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('double_pendulum.png', dpi=150)
plt.show()
```

### Python — Quantum Infinite Well Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

L = 1.0            # well width (nm)
m = 9.109e-31      # electron mass (kg)
hbar = 1.055e-34   # reduced Planck constant

x = np.linspace(0, L, 500)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for n in range(1, 5):
    # Wavefunction
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    ax1.plot(x, psi + n * 2, label=f'n={n}')
    ax1.axhline(y=n * 2, color='gray', linestyle='--', alpha=0.3)

    # Probability density
    prob = psi**2
    ax2.plot(x, prob + n * 2, label=f'n={n}')
    ax2.fill_between(x, n * 2, prob + n * 2, alpha=0.2)
    ax2.axhline(y=n * 2, color='gray', linestyle='--', alpha=0.3)

ax1.set_xlabel('x / L')
ax1.set_ylabel('ψₙ(x) (offset)')
ax1.set_title('Wavefunctions')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.set_xlabel('x / L')
ax2.set_ylabel('|ψₙ(x)|² (offset)')
ax2.set_title('Probability Densities')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle('Particle in Infinite Potential Well', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('quantum_well.png', dpi=150)
plt.show()
```

## Fundamental Constants

```
Speed of light:             c  = 2.998 × 10⁸ m/s
Gravitational constant:     G  = 6.674 × 10⁻¹¹ N·m²/kg²
Planck's constant:          h  = 6.626 × 10⁻³⁴ J·s
Reduced Planck's constant:  ℏ  = 1.055 × 10⁻³⁴ J·s
Boltzmann constant:         k_B = 1.381 × 10⁻²³ J/K
Avogadro's number:          N_A = 6.022 × 10²³ mol⁻¹
Elementary charge:          e  = 1.602 × 10⁻¹⁹ C
Electron mass:              mₑ = 9.109 × 10⁻³¹ kg
Proton mass:                mₚ = 1.673 × 10⁻²⁷ kg
Vacuum permittivity:        ε₀ = 8.854 × 10⁻¹² F/m
Vacuum permeability:        μ₀ = 4π × 10⁻⁷ H/m
Stefan-Boltzmann constant:  σ  = 5.670 × 10⁻⁸ W/(m²·K⁴)
Gas constant:               R  = 8.314 J/(mol·K)
Coulomb constant:           k  = 8.988 × 10⁹ N·m²/C²
Standard gravity:           g  = 9.807 m/s²
Atomic mass unit:           u  = 1.661 × 10⁻²⁷ kg
```

## Unit Conversions

```
Energy:    1 eV = 1.602 × 10⁻¹⁹ J
           1 cal = 4.186 J
           1 kWh = 3.6 × 10⁶ J

Length:    1 Å = 10⁻¹⁰ m
           1 nm = 10⁻⁹ m
           1 ly = 9.461 × 10¹⁵ m
           1 AU = 1.496 × 10¹¹ m
           1 pc = 3.086 × 10¹⁶ m

Pressure:  1 atm = 101,325 Pa = 760 mmHg
           1 bar = 10⁵ Pa

Temperature: T(K) = T(°C) + 273.15
             T(°F) = 9/5 · T(°C) + 32

Mass:      1 u = 931.5 MeV/c²

Angle:     1 rad = 180°/π ≈ 57.296°
```

## Best Practices

### Problem Solving

- Always draw a diagram: free-body diagrams, circuit diagrams, ray diagrams, spacetime diagrams
- Identify the system and choose a coordinate system before writing equations
- Work with symbols as long as possible; substitute numbers at the end
- Check dimensional consistency of every equation
- Verify answers with limiting cases (e.g., what happens as m → 0, v → 0, θ → 0?)
- Compare numerical results to known orders of magnitude

### Dimensional Analysis

- Every term in an equation must have the same dimensions
- Use dimensional analysis to guess functional forms (Buckingham π theorem)
- When stuck, listing dimensions of all quantities often reveals the relationship
- Dimensionless ratios (Reynolds number, Mach number, etc.) indicate regime changes

### Approximations

- State approximations explicitly (small angle, non-relativistic, ideal gas, etc.)
- Know when approximations break down and quantify the error
- Use Taylor expansions for small perturbations: sin θ ≈ θ, cos θ ≈ 1 - θ²/2, (1+x)ⁿ ≈ 1+nx
- In relativity: for v ≪ c, γ ≈ 1 + v²/(2c²)

### Numerical Methods

- Use RK4 or higher-order integrators for dynamical systems (not Euler for accuracy)
- Check energy conservation in conservative systems as a validation
- Use adaptive step-size methods (`solve_ivp` with RK45) for chaotic systems
- Validate numerical results against analytical solutions in known limits
- Use SI units consistently in code to avoid conversion errors

### Common Mistakes to Avoid

- Confusing velocity and speed, displacement and distance
- Forgetting that forces are vectors — always resolve into components
- Using formulas for constant acceleration when acceleration varies
- Mixing up path-dependent (work, heat) and state quantities (energy, entropy)
- Ignoring sign conventions (especially in optics, thermodynamics, and circuits)
- Applying conservation laws to non-isolated systems
- Using non-inertial frames without adding pseudo-forces

## Troubleshooting

### Units Don't Match

- Trace back through the derivation checking dimensions at each step
- Common culprits: missing factors of 2π vs ω, radians vs degrees, eV vs Joules
- Use a unit-aware library (Pint for Python, Unitful for Julia) in computational work

### Answer Is Orders of Magnitude Off

- Check for missing powers of 10 in constants (e.g., using G without ×10⁻¹¹)
- Verify unit prefixes: nano (10⁻⁹), micro (10⁻⁶), milli (10⁻³), kilo (10³), mega (10⁶)
- Confirm you're using the correct constant (k_B vs R, h vs ℏ)

### Simulation Diverges or Produces Nonsense

- Reduce the time step and compare results
- Switch from Euler to RK4 or adaptive method
- Check initial conditions and boundary conditions
- Verify the equations of motion against a textbook derivation
- Plot intermediate quantities (energy, momentum) to find where conservation breaks

### Conceptual Confusion

- Draw the scenario from multiple reference frames
- Identify which quantities are conserved and which are not
- Distinguish between instantaneous and average values
- Re-read the problem statement — many errors come from misinterpreting what is asked

## Integration Points

- **Computation**: Python (NumPy, SciPy, Matplotlib, SymPy), MATLAB, Mathematica, Julia
- **Simulation**: VPython/GlowScript, PhET, Blender (physics engine), Unity/Godot
- **Symbolic math**: SymPy, Mathematica, Wolfram Alpha, Maxima
- **Data analysis**: curve fitting, error propagation, Monte Carlo methods
- **Visualization**: Matplotlib, Plotly, Manim (3Blue1Brown-style animations)
- **Textbook references**: Halliday/Resnick, Griffiths (EM, QM), Kleppner/Kolenkow, Taylor, Sakurai
- **Online resources**: HyperPhysics, Physics LibreTexts, MIT OCW, Khan Academy
