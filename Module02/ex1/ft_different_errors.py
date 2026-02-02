def garden_operations(error_type):
    """
    Triggers different built-in exception scenarios based on input.
    Supports: 'value', 'zero', 'file', 'key'.
    """
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        10 / 0
    elif error_type == "file":
        open("missing.txt")
    elif error_type == "key":
        garden = {"plant": "tomato"}
        garden["missing_plant"]


def test_error_types():
    """
    Demonstrates catching built-in exceptions individually and together.
    """
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("Testing multiple errors together...")
    try:
        garden_operations("zero")
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
