from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost if cost > 0 else 0
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        pass

    play = abstractmethod(play)

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "")
        }

    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int):
            return available_mana >= self.cost
        raise ValueError("int Error")
