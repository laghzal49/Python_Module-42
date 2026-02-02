class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant-related error occurs."""
    pass


class WaterError(GardenError):
    """Raised when a water-related error occurs."""
    pass


class GardenManager:
    """
    Manages plants and handles garden operations with proper error handling.
    """

    def __init__(self):
        """Initialize the garden manager with an empty plant list."""
        self.plants = []

    def add_plant(self, name):
        """
        Add a plant to the garden.

        Raises:
            PlantError: If the plant name is empty.
        """
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants += [name]
        print(f"Added {name} successfully")

    def water_plants(self):
        """
        Water all plants in the garden.

        Uses a finally block to ensure cleanup happens even if an error occurs.

        Raises:
            WaterError: If there are no plants to water.
        """
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name, water_level, sunlight):
        """
        Check the health of a plant based on water and sunlight levels.

        Raises:
            PlantError: If the plant name is empty.
            WaterError: If the water level is outside the range 1–10.
            GardenError: If sunlight hours are outside the range 2–12.
        """
        if not name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if sunlight < 2:
            raise GardenError(f"Sunlight hours {sunlight} is too low (min 2)")
        if sunlight > 12:
            raise GardenError(
                f"Sunlight hours {sunlight} is too high (max 12)")


def test_garden_management():
    """
    Test function demonstrating the full garden management system,
    including error handling and recovery.
    """
    print("=== Garden Management System ===\n")
    gm = GardenManager()

    print("Adding plants...")
    try:
        gm.add_plant("tomato")
        gm.add_plant("lettuce")
        gm.add_plant("")
    except GardenError as e:
        print(f"Caught error: {e}")

    print("\nChecking plant health...")
    try:
        gm.check_plant_health("tomato", 5, 8)
        gm.check_plant_health("lettuce", 15, 10)
    except GardenError as e:
        print(f"Caught error: {e}")

    print("\nWatering plants...")
    try:
        gm.water_plants()
    except GardenError as e:
        print(f"Caught error: {e}")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
