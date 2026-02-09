from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass

    create_themed_deck = abstractmethod(create_themed_deck)
    get_supported_types = abstractmethod(get_supported_types)
    create_artifact = abstractmethod(create_artifact)
    create_spell = abstractmethod(create_spell)
    create_creature = abstractmethod(create_creature)
