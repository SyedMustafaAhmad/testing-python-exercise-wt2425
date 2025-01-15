"""
Tests for functions in class SolveDiffusion2D
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from diffusion2d import SolveDiffusion2D


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 2.0, 3.0, 0.5, 0.5
    expected_nx = int(w / dx)
    expected_ny = int(h / dy)
    solver.initialize_domain(w, h, dx, dy)
    assert solver.nx == expected_nx
    assert solver.ny == expected_ny


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    D, T_cold, T_hot = 2.5, 250.0, 750.0
    solver.dx, solver.dy = 0.1, 0.1
    solver.initialize_physical_parameters(D, T_cold, T_hot)
    expected_dt = (solver.dx * solver.dy) / (2 * D*10 * (solver.dx + solver.dy))
    assert solver.dt == expected_dt, f"Expected dt: {expected_dt}, but got: {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    D, T_cold, T_hot = 2.5, 250.0, 750.0
    solver.D = D
    solver.T_cold = T_cold
    solver.T_hot = T_hot
    solver.dx = 0.1
    solver.dy = 0.1
    solver.initialize_physical_parameters(D, T_cold, T_hot)
    # Calculate expected dt based on the stability criterion
    expected_dt = (solver.dx * solver.dy) / (2 * D*10 * (solver.dx + solver.dy))
    assert solver.dt == expected_dt
