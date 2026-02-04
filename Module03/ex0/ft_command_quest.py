import sys


def main():
    """
    Demonstrate command-line argument processing using sys.argv.
    """
    print("=== Command Quest ===")
    len_t = len(sys.argv)

    if (len_t) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if (len_t) > 1:
        print(f"Arguments received: {len_t - 1}")
    for i in range(1, len_t):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len_t}")


if __name__ == "__main__":
    main()
