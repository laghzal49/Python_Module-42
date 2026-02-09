from ex2.EliteCard import EliteCard


def main() -> None:
    try:
        print("=== DataDeck Ability System ===")

        elite = EliteCard("Arcane Warrior", 4,
                          "Epic", attack_power=5, health=8, mana_pool=3)

        print("\nEliteCard capabilities:")
        print("- Card:", ["play", "get_card_info", "is_playable"])
        print("- Combatable:", ["attack", "defend", "get_combat_stats"])
        print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])

        print("\nPlaying Arcane Warrior (Elite Card):")
        print(elite.play({}))

        print("\nCombat phase:")
        print("Attack result:", elite.attack("Enemy"))
        print("Defense result:", elite.defend(2))

        print("\nMagic phase:")
        print("Spell cast:", elite.cast_spell("Fireball",
              ["Enemy1", "Enemy2"]))
        print("Mana channel:", elite.channel_mana(3))

        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(f"Erorr in {e}")


if __name__ == "__main__":
    main()
