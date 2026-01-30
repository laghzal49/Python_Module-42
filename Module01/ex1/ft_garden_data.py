class Plant:
    """
    A class to represent a plant in the community garden.
    """

    def __init__(self, name, height, age):
        """
        Initialize the plant with its basic characteristics.
        """
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        """
        Print the plant's information in a formatted string.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants1 = Plant("Rose", 25, 30)
    plants2 = Plant("Sunflower", 80, 45)
    plants3 = Plant("Cactus", 15, 120)

    print("=== Community Garden Data Report ===")
    plants1.display_info()
    plants2.display_info()
    plants3.display_info()
