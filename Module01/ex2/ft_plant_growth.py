class Plant:
    """
    A class to represent a plant and simulate its growth over time.
    """

    def __init__(self, name, height, age) -> None:
        """Initialize the plant's attributes."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increase the plant's height by a specific amount."""
        self.height += cm

    def ageadd(self, days: int) -> None:
        """Increase the plant's age by a specific amount."""
        self.age += days

    def get_info(self) -> None:
        """Print a string containing current plant status."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    print("=== Day 7 ===")
    rose.grow(6)
    rose.ageadd(7)
    rose.get_info()
    print("Growth this week: +6cm")
