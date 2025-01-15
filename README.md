# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

After changing the calculation from self.nx = int(w / dx) to self.nx = int(h / dx)
```
============================================================================================== FAILURES ===============================================================================================
_______________________________________________________________________________________ test_initialize_domain ________________________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w, h, dx, dy = 2.0, 3.0, 0.5, 0.5
        expected_nx = int(w / dx)
        expected_ny = int(h / dy)
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == expected_nx
E       assert 6 == 4
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x7e8d54136b10>.nx

tests/unit/test_diffusion2d_functions.py:20: AssertionError
```

### unittest log


#### With Errors

```
(venv) syedm@xps9315:~/workspace/sse/python_testing/testing-python-exercise-wt2425$ pytest tests/unit/test_diffusion2d_functions.py
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/syedm/workspace/sse/python_testing
configfile: pytest.ini
collected 3 items                                                                                                                                                                                     

tests/unit/test_diffusion2d_functions.py::test_initialize_domain PASSED                                                                                                                         [ 33%]
tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters FAILED                                                                                                            [ 66%]
tests/unit/test_diffusion2d_functions.py::test_set_initial_condition FAILED                                                                                                                     [100%]

============================================================================================== FAILURES ===============================================================================================
_________________________________________________________________________________ test_initialize_physical_parameters _________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        D, T_cold, T_hot = 2.5, 250.0, 750.0
        solver.dx, solver.dy = 0.1, 0.1
        solver.initialize_physical_parameters(D, T_cold, T_hot)
        expected_dt = (solver.dx * solver.dy) / (2 * D * (solver.dx + solver.dy))
>       assert solver.dt == expected_dt, f"Expected dt: {expected_dt}, but got: {solver.dt}"
E       AssertionError: Expected dt: 0.010000000000000002, but got: 0.0010000000000000002
E       assert 0.0010000000000000002 == 0.010000000000000002
E        +  where 0.0010000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x71c381b91f10>.dt

tests/unit/test_diffusion2d_functions.py:33: AssertionError
---------------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------------
dt = 0.0010000000000000002
_____________________________________________________________________________________ test_set_initial_condition ______________________________________________________________________________________

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
        expected_dt = (solver.dx * solver.dy) / (2 * D * (solver.dx + solver.dy))
>       assert solver.dt == expected_dt
E       assert 0.0010000000000000002 == 0.010000000000000002
E        +  where 0.0010000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x71c35f877230>.dt

tests/unit/test_diffusion2d_functions.py:50: AssertionError
---------------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------------
dt = 0.0010000000000000002
======================================================================================= short test summary info =======================================================================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - AssertionError: Expected dt: 0.010000000000000002, but got: 0.0010000000000000002
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 0.0010000000000000002 == 0.010000000000000002
===================================================================================== 2 failed, 1 passed in 0.59s =====================================================================================
```

#### With Resolved Errors
The errors were resolved by multiplying D by 10 since the above error log shows difference 10x in comparitive assertion
```
(venv) syedm@xps9315:~/workspace/sse/python_testing/testing-python-exercise-wt2425$ pytest tests/unit/test_diffusion2d_functions.py
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/syedm/workspace/sse/python_testing
configfile: pytest.ini
collected 3 items                                                                                                                                                                                     

tests/unit/test_diffusion2d_functions.py::test_initialize_domain PASSED                                                                                                                         [ 33%]
tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED                                                                                                            [ 66%]
tests/unit/test_diffusion2d_functions.py::test_set_initial_condition PASSED                                                                                                                     [100%]

========================================================================================== 3 passed in 0.54s ==========================================================================================
```

### Integration Test Log

### With Error
Intentionally placing wrong value for T_cold = 100.0
```
(venv) syedm@xps9315:~/workspace/sse/python_testing/testing-python-exercise-wt2425$ pytest
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/syedm/workspace/sse/python_testing
configfile: pytest.ini
collected 5 items                                                                                                                                                                                     

tests/integration/test_diffusion2d.py::test_initialize_physical_parameters FAILED                                                                                                               [ 20%]
tests/integration/test_diffusion2d.py::test_set_initial_condition PASSED                                                                                                                        [ 40%]
tests/unit/test_diffusion2d_functions.py::test_initialize_domain PASSED                                                                                                                         [ 60%]
tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED                                                                                                            [ 80%]
tests/unit/test_diffusion2d_functions.py::test_set_initial_condition PASSED                                                                                                                     [100%]

============================================================================================== FAILURES ===============================================================================================
_________________________________________________________________________________ test_initialize_physical_parameters _________________________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w, h, dx, dy = 2.0, 3.0, 0.1, 0.1
        D, T_cold, T_hot = 2.5, 250.0, 750.0
        solver.initialize_domain(w, h, dx, dy)
        solver.initialize_physical_parameters(D, T_cold, T_hot)
    
        # Intentionally wrong value
        T_cold = 100.0
    
        dx2, dy2 = solver.dx**2, solver.dy**2
        expected_dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    
        assert solver.D == D, f"Expected D: {D}, but got: {solver.D}"
>       assert solver.T_cold == T_cold, f"Expected T_cold: {T_cold}, but got: {solver.T_cold}"
E       AssertionError: Expected T_cold: 100.0, but got: 250.0
E       assert 250.0 == 100.0
E        +  where 250.0 = <diffusion2d.SolveDiffusion2D object at 0x7433a0439d60>.T_cold

tests/integration/test_diffusion2d.py:28: AssertionError
---------------------------------------------------------------------------------------- Captured stdout call -----------------------------------------------------------------------------------------
dt = 0.0010000000000000002
======================================================================================= short test summary info =======================================================================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - AssertionError: Expected T_cold: 100.0, but got: 250.0
===================================================================================== 1 failed, 4 passed in 0.60s =====================================================================================
```

### After Fixes
```
(venv) syedm@xps9315:~/workspace/sse/python_testing/testing-python-exercise-wt2425$ pytest
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/syedm/workspace/sse/python_testing
configfile: pytest.ini
collected 5 items                                                                                                                                                                                     

tests/integration/test_diffusion2d.py::test_initialize_physical_parameters PASSED                                                                                                               [ 20%]
tests/integration/test_diffusion2d.py::test_set_initial_condition PASSED                                                                                                                        [ 40%]
tests/unit/test_diffusion2d_functions.py::test_initialize_domain PASSED                                                                                                                         [ 60%]
tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED                                                                                                            [ 80%]
tests/unit/test_diffusion2d_functions.py::test_set_initial_condition PASSED                                                                                                                     [100%]

========================================================================================== 5 passed in 0.56s ==========================================================================================
```

### Tox
```
(venv) syedm@xps9315:~/workspace/sse/python_testing/testing-python-exercise-wt2425$ tox
unittest: commands[0]> pytest tests/unit/test_diffusion2d_functions.py
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
cachedir: .tox/unittest/.pytest_cache
rootdir: /home/syedm/workspace/sse/python_testing/testing-python-exercise-wt2425
configfile: pytest.ini
collected 3 items                                                                                                                                                                                     

tests/unit/test_diffusion2d_functions.py::test_initialize_domain PASSED                                                                                                                         [ 33%]
tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED                                                                                                            [ 66%]
tests/unit/test_diffusion2d_functions.py::test_set_initial_condition PASSED                                                                                                                     [100%]

========================================================================================== 3 passed in 0.68s ==========================================================================================
unittest: OK ✔ in 1.12 seconds
integrationtest: commands[0]> pytest tests/integration/test_diffusion2d.py
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
cachedir: .tox/integrationtest/.pytest_cache
rootdir: /home/syedm/workspace/sse/python_testing/testing-python-exercise-wt2425
configfile: pytest.ini
collected 2 items                                                                                                                                                                                     

tests/integration/test_diffusion2d.py::test_initialize_physical_parameters PASSED                                                                                                               [ 50%]
tests/integration/test_diffusion2d.py::test_set_initial_condition PASSED                                                                                                                        [100%]

========================================================================================== 2 passed in 0.71s ==========================================================================================
integrationtest: OK ✔ in 1.2 seconds
coverage: commands[0]> coverage run -m pytest
========================================================================================= test session starts =========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.4, pluggy-1.5.0
cachedir: .tox/coverage/.pytest_cache
rootdir: /home/syedm/workspace/sse/python_testing/testing-python-exercise-wt2425
configfile: pytest.ini
collected 5 items                                                                                                                                                                                     

tests/integration/test_diffusion2d.py::test_initialize_physical_parameters PASSED                                                                                                               [ 20%]
tests/integration/test_diffusion2d.py::test_set_initial_condition PASSED                                                                                                                        [ 40%]
tests/unit/test_diffusion2d_functions.py::test_initialize_domain PASSED                                                                                                                         [ 60%]
tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED                                                                                                            [ 80%]
tests/unit/test_diffusion2d_functions.py::test_set_initial_condition PASSED                                                                                                                     [100%]

========================================================================================== 5 passed in 2.01s ==========================================================================================
coverage: commands[1]> coverage html
Wrote HTML report to htmlcov/index.html
coverage: commands[2]> coverage report
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
diffusion2d.py                                82     32    61%
tests/integration/test_diffusion2d.py         37      0   100%
tests/unit/test_diffusion2d_functions.py      30      0   100%
--------------------------------------------------------------
TOTAL                                        149     32    79%
  unittest: OK (1.12=setup[0.04]+cmd[1.08] seconds)
  integrationtest: OK (1.20=setup[0.01]+cmd[1.19] seconds)
  coverage: OK (3.15=setup[0.02]+cmd[2.64,0.27,0.22] seconds)
  congratulations :) (5.57 seconds)
```


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
