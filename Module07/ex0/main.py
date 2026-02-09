from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("=== DataDeck Card Foundation ===")
        print("Testing Abstract Base Class Design:\n")

        creature = CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity="Legendary",
            attack=7,
            health=5
        )

        print("CreatureCard Info:")
        print(creature.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        print("Playable:", creature.is_playable(6))
        print("Play result:", creature.play({}))

        print("\nFire Dragon attacks Goblin Warrior:")
        print(creature.attack_target("Goblin Warrior"))

        print("\nTesting insufficient mana (3 available):")
        print("Playable:", creature.is_playable(3))

        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Error in {e}")


if __name__ == "__main__":
    main()
