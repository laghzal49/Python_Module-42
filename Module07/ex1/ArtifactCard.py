from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int):
            raise ValueError("Durability must be an integer")
        if durability <= 0:
            raise ValueError("Durability must be a positive integer")
        if not isinstance(effect, str) or not effect.strip():
            raise ValueError("Effect must be a non-empty string")

        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "Artifact is broken",
            }

        self.durability -= 1
        return {
            "artifact": self.name,
            "activated": True,
            "effect": self.effect,
            "durability_left": self.durability,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
