def water_plants(plant_list):
    """
    Waters all plants in the given list and always cleans up.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                print("Error: Cannot water None - invalid plant!")
                return
            print("Watering " + plant)
    except TypeError:
        print("Error: Invalid plant list!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Demonstrates normal watering and error handling.
    """
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce"])
    print("Watering completed successfully!")

    print("Testing with error...")
    water_plants(["tomato", None])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
