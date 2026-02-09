from abc import ABC, abstractmethod


class GameStrategy(ABC):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets: list) -> list:
        pass

    execute_turn = abstractmethod(execute_turn)
    get_strategy_name = abstractmethod(get_strategy_name)
    prioritize_targets = abstractmethod(prioritize_targets)
