import sys
import importlib
from typing import List, Tuple


def check_dependencies(requirements: List[Tuple[str, str]]) -> bool:
    """Check if required packages are installed."""
    print("Checking dependencies:")
    all_passed = True
    for module_name, description in requirements:
        try:
            mod = importlib.import_module(module_name)
            # getattr gets __version__ from module, falls back to 'unknown'
            version = getattr(mod, '__version__', 'unknown')
            print(f"[OK] {module_name} ({version}) - {description}")
        except ImportError:
            # module not installed — mark as failed
            print(f"[FAIL] {module_name} is missing.")
            all_passed = False
    return all_passed  # False if any module missing


def main() -> None:
    """main execution function — checks dependencies, establishes connection"""
    print("LOADING STATUS: Loading programs...")

    required_modules = [
        ("pandas",     "Data manipulation ready"),
        ("requests",   "Network access ready"),
        ("matplotlib", "Visualization ready"),
        ("numpy",      "Numerical computation ready")
    ]

    # exit with code 1 (error) if any package is missing
    if not check_dependencies(required_modules):
        print("\nSYSTEM ERROR: Required programs are not loaded.")
        sys.exit(1)

    # import AFTER confirming packages exist — avoids crash at top level
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests

    print("\nEstablishing connection...")

    # timeout=5 — give up if no response within 5 seconds
    response = requests.get("https://httpbin.org/get", timeout=5)

    # status 200 = success, anything else = problem
    if response is None or response.status_code != 200:
        print("[FAIL] Network connection failed.")
        sys.exit(1)

    print("[OK] Connection secured.")

    # 1000 rows, 2 columns of random floats between 0.0 and 1.0
    data = np.random.rand(1000, 2)
    df = pd.DataFrame(data, columns=['Signal_X', 'Signal_Y'])
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Signal_X'], df['Signal_Y'], color="#F80000")
    plt.title('Matrix Signal Anomalies')

    # save chart as image instead of displaying it
    plt.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    # only runs when executed directly, not when imported
    main()
