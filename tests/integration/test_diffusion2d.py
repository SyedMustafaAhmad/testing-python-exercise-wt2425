"""
Tests for functionality checks in class SolveDiffusion2D
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from diffusion2d import SolveDiffusion2D
import numpy as np


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 2.0, 3.0, 0.1, 0.1
    D, T_cold, T_hot = 2.5, 250.0, 750.0
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(D, T_cold, T_hot)

    dx2, dy2 = solver.dx**2, solver.dy**2
    expected_dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    assert solver.D == D, f"Expected D: {D}, but got: {solver.D}"
    assert solver.T_cold == T_cold, f"Expected T_cold: {T_cold}, but got: {solver.T_cold}"
    assert solver.T_hot == T_hot, f"Expected T_hot: {T_hot}, but got: {solver.T_hot}"
    assert np.isclose(solver.dt, expected_dt), f"Expected dt: {expected_dt}, but got: {solver.dt}"

    # debug
    print(f"Expected dt: {expected_dt}, Computed dt: {solver.dt}")



def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    # Create an instance of the solver
    solver = SolveDiffusion2D()

    w, h, dx, dy = 10.0, 10.0, 1.0, 1.0
    T_cold, T_hot = 250.0, 750.0
    solver.initialize_domain(w, h, dx, dy)
    solver.T_cold = T_cold
    solver.T_hot = T_hot

    # to set initial condition
    u = solver.set_initial_condition()

    # expected result
    expected_u = np.full((solver.nx, solver.ny), T_cold)
    r, cx, cy = 2, 5, 5  # Circle radius and center
    r2 = r ** 2

    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r2:
                expected_u[i, j] = T_hot

    # Debug
    print(f"Expected u:\n{expected_u}")
    print(f"Actual u:\n{u}")
    assert np.array_equal(u, expected_u), "The set_initial_condition method did not produce the expected output."
