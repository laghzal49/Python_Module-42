class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for problems with plants."""
    pass


class WaterError(GardenError):
    """Exception raised for problems with watering."""
    pass


def check_garden_status(issue_type):
    """
    Helper function to raise custom errors based on input.
    """
    if issue_type == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif issue_type == "water":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """
    Docstring for Testing !
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")

    try:
        check_garden_status("plant")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")

    try:
        check_garden_status("water")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    issues = ["plant", "water"]

    for issue in issues:
        try:
            check_garden_status(issue)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
