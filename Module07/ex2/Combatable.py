from abc import ABC, abstractmethod


class Combatable(ABC):
    def attack(self, target) -> dict:
        ...

    def defend(self, incoming_damage: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...

    attack = abstractmethod(attack)
    defend = abstractmethod(defend)
    get_combat_stats = abstractmethod(get_combat_stats)
