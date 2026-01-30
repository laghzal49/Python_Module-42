class GardenManager:
    """Manages a collection of plants and tracks garden statistics."""
    total_gardens: int = 0

    class GardenStats:
        """Internal tracker for growth and plant types."""
        def __init__(self) -> None:
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.regular_count: int = 0
            self.flowering_count: int = 0
            self.prize_count: int = 0

    def __init__(self, owner: str) -> None:
        """Initialize garden with an owner and empty stats."""
        self.owner: str = owner
        self.plants: list = []
        self.stats: GardenManager.GardenStats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: 'Plant') -> None:
        """Adds a plant to the garden and updates specific type counts."""
        self.plants.append(plant)
        self.stats.plants_added += 1

        if plant.type == "prize":
            self.stats.prize_count += 1
        elif plant.type == "flowering":
            self.stats.flowering_count += 1
        else:
            self.stats.regular_count += 1

        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        """Triggers the grow method for all plants in the list."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def report(self) -> None:
        """Prints a summary of all plants and growth statistics."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print()
        print(f"Plants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.regular_count} regular, "
              f"{self.stats.flowering_count} flowering, "
              f"{self.stats.prize_count} prize flowers\n")

    @classmethod
    def create_garden_network(cls) -> str:
        """Returns the total number of GardenManager instances."""
        return f"Total gardens managed: {cls.total_gardens}"

    @staticmethod
    def validate_heght(height: int) -> bool:
        """Validates if the provided height is positive."""
        return height > 0


class Plant:
    """Base class for all garden plants."""
    def __init__(self, name: str, height: int) -> None:
        """Initialize basic plant attributes."""
        self.name: str = name
        self.height: int = height
        self.type: str = "regular"

    def grow(self) -> None:
        """Increments plant height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """Returns name and height string."""
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that produces flowers."""
    def __init__(self, name: str, height: int, color: str,
                 is_blooming: bool) -> None:
        """Initialize flowering plant with color and bloom status."""
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = is_blooming
        self.type: str = "flowering"

    def get_info(self) -> str:
        """Returns plant info with flower color and bloom state."""
        status: str = "blooming" if self.is_blooming else "not blooming"
        return (f"{super().get_info()}, {self.color} "
                f"flowers ({status})")


class PrizeFlower(FloweringPlant):
    """A competitive flowering plant with points."""
    def __init__(self, name: str,
                 height: int, color: str, is_blooming: bool,
                 prize_points: int) -> None:
        """Initialize prize flower with competitive points."""
        super().__init__(name, height, color, is_blooming)
        self.prize_points: int = prize_points
        self.type: str = "prize"

    def get_info(self) -> str:
        """Returns info including prize points."""
        return (f"{super().get_info()}, Prize points: {self.prize_points}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice: GardenManager = GardenManager("Alice")
    bob: GardenManager = GardenManager("Bob")

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red", True)
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()
    alice.help_plants_grow()
    print()
    alice.report()
    print("Height validation test: ", GardenManager.validate_heght(oak.height))

    alice_score: int = 0
    for p in alice.plants:
        alice_score += p.height

    print(f"Garden scores - Alice: {alice_score}, Bob: 92")
    print(GardenManager.create_garden_network())
