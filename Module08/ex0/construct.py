import sys


def check_env() -> None:
    """Checking the Env"""
    #   sys.base.prefix is a Varible alwyas point the orig env dir
    #  sys.prefix is a var pointing to current env dir

    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        # sys.executable Varible tell y what python version is runing
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!", file=sys.stderr)
        print(
            "The machines can see everything you install.\n"
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\n"
            "Scripts\n"
            "activate # On Windows\n"
        )
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: You're in the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in the construct!")
        print("Safe to install packages without ")
        print("affecting the global environment.")
        print(f"Package installation path: {sys.prefix}\n")


if __name__ == "__main__":
    """Entry Point"""
    check_env()
