# ex3/main.py
from __future__ import annotations

import random

from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main() -> None:
    try:
        print("=== DataDeck Game Engine ===")
        print("Configuring Fantasy Card Game...")

        engine = GameEngine()
        factory = FantasyCardFactory(rng=random.Random(42))
        strategy = AggressiveStrategy(starting_mana=6)

        engine.configure_engine(factory, strategy)

        print(f"Factory: {type(factory).__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

        print("Simulating aggressive turn...")
        result = engine.simulate_turn()

        print("Hand:", result["hand"])
        print("Turn execution:")
        print(result["turn_execution"])
        print("Game Report:")
        print(result["game_report"])
        print("Abstract Factory + Strategy Pattern"
              ": Maximum flexibility achieved!")
    except Exception as e:
        print(f"Error in {e}")


if __name__ == "__main__":
    main()
