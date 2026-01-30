class SecurePlant:
    """
    A plant class that protects it data using private attributes and validation
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name and private height/age."""
        self.name: str = name
        self.__height: int = height
        self.__age: int = age

    def set_height(self, value: int) -> None:
        """Validates and sets the private height attribute."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def get_height(self) -> int:
        """Returns the private height value."""
        return self.__height

    def set_age(self, value: int) -> None:
        """Validates and sets the private age attribute."""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def get_age(self) -> int:
        """Returns the private age value."""
        return self.__age

    def display_status(self) -> None:
        """Prints the current identity and dimensions of the plant."""
        print("Current plant:", self.name, end=" ")
        print(f"({self.__height}cm {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p: SecurePlant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {p.name}")
    p.set_height(25)
    p.set_age(30)
    print()
    p.set_height(-5)
    print()
    p.display_status()
