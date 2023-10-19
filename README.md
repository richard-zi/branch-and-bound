# Branch-and-Bound Algorithm

## Description

This repository contains two Python scripts implementing the Branch-and-Bound algorithm to solve linear optimization problems. The two scripts utilize different libraries to solve the optimization problems:

1. **branch-and-bound-scipy.py**: This script uses the `scipy.optimize.linprog` function from the `SciPy` library.
2. **branch-and-bound-xpress.py**: This script uses the `xpress` library.

Both scripts also include functionalities for visualizing the solution process using the `networkx` and `matplotlib` libraries.

## Prerequisites

- Python 3.x
- SciPy
- Matplotlib
- NetworkX
- Xpress (only for `branch-and-bound-xpress.py`)

## Installing Prerequisites

You can install the necessary packages using `pip`:

```bash
pip install scipy matplotlib networkx xpress
```

## Execution of Scripts

You can execute each script from the command line:

```bash
python3 branch-and-bound-scipy.py
```

or

```bash
python3 branch-and-bound-xpress.py
```

## Visualization

The scripts also generate a visualization of the Branch-and-Bound process, showing the search tree and the solutions found.
