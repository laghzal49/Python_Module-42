class Plant:
    """
    A class representing a plant with a global counter to track
    the total number of plants created.
    """
    plantnumber = 0

    def __init__(self, name, height, age):
        """
        Initialize a new plant and increment the global factory counter.
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.plantnumber += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days old)")


if __name__ == "__main__":
    print("=== Community Garden Data Report ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    print("")
    print(f"Total plants created: {Plant.plantnumber}")
