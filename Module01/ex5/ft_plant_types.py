class Plant:
    """
    Base class representing common features of all plants.

    Attributes:
        name (str): The common name of the plant.
        _height (int): The height of the plant in centimeters.
        _age (int): The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): Height in cm.
            age (int): Age in days.
        """
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_info(self) -> str:
        """
        Returns a formatted string containing general information about plant.

        Returns:
            str: Description of the plant name, class, height, and age.
        """
        return f"""{self.name} ({self.__class__.__name__}): {self._height}cm,\
 {self._age} days"""


class Flower(Plant):
    """
    Represents a flowering plant, inheriting from Plant.

    Attributes:
        color (str): The primary color of the flower petals.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initializes a Flower instance.

        Args:
            name (str): The name of the flower.
            height (int): Height in cm.
            age (int): Age in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Prints a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """
        Returns extended information including the flower color.

        Returns:
            str: Plant info plus the flower color.
        """
        return f"{super().get_info()}, {self.color} color"


class Tree(Plant):
    """
    Represents a tree, inheriting from Plant.

    Attributes:
        trunk_diameter (int): The diameter of the tree trunk in centimeters.
    """
    def __init__(self, name: str, height: int, age: int, diametr: int) -> None:
        """
        Initializes a Tree instance.

        Args:
            name (str): The name of the tree.
            height (int): Height in cm.
            age (int): Age in days.
            trunk_diameter (int): Diameter in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = diametr

    def get_info(self) -> str:
        """
        Returns extended information including trunk diameter.

        Returns:
            str: Plant info plus the trunk diameter.
        """
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> None:
        """
        Calculates and prints the estimated shade area based on trunk diameter.
        """
        shade_area: float = self.trunk_diameter * 1.57
        print(f"{self.name} provides {int(shade_area)} square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable plant, inheriting from Plant.

    Attributes:
        harveseason: The season when the vegetable is ready to be picked.
        nutrition : The primary vitamin or nutrient found in the vegetable.
    """
    def __init__(
            self, name: str,
            height: int, age: int, season: str, nutrition: str) -> None:
        """
        Initializes a Vegetable instance.

        Args:
            name (str): The name of the vegetable.
            height (int): Height in cm.
            age (int): Age in days.
            harvest_season (str): The season of harvest.
            nutrition (str): Key nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutrition: str = nutrition

    def get_info(self) -> str:
        """
        Returns extended information including the harvest season.

        Returns:
            str: Plant info plus the harvest season.
        """
        return f"{super().get_info()}, {self.harvest_season} harvest"

    def nutritional_value(self) -> None:
        """
        Prints a message describing the nutritional content of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutrition}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose: Flower = Flower("Rose", 25, 30, "red")
    lily: Flower = Flower("Lily", 35, 20, "white")

    oak: Tree = Tree("Oak", 500, 1825, 50)
    pine: Tree = Tree("Pine", 400, 1460, 40)

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot: Vegetable = Vegetable("Carrot", 20, 75, "autumn", "vitamin A")

    print(rose.get_info())
    rose.bloom()
    print("")
    print(oak.get_info())
    oak.produce_shade()
    print("")
    print(tomato.get_info())
    tomato.nutritional_value()
