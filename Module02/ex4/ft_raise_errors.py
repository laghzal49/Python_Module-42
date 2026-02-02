def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check the health of a plant based on
      its name, water level, and sunlight hours.

    Raises:
        ValueError: If any input is invalid or out of the allowed range.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Test function demonstrating error raising and handling
    for the check_plant_health function.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        message = check_plant_health("tomato", 5, 8)
        print(message)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("\nTesting empty plant name...")
    try:
        message = check_plant_health("", 5, 8)
        print(message)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("\nTesting bad water level...")
    try:
        message = check_plant_health("tomato", 15, 8)
        print(message)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("\nTesting bad sunlight hours...")
    try:
        message = check_plant_health("tomato", 5, 0)
        print(message)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
