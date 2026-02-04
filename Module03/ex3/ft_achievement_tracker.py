

def main():
    """
    Achievement Tracker System
    This module provides utilities toe player achievements using set theory
    identifying unique, common, and rare player milestones.
    """
    print("=== Achievement Tracker System ==\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print()
    print("=== Achievement Analytics ===")
    unique = charlie.union(alice, bob)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")

    commun = alice.intersection(bob, charlie)
    print(f"Common to all players: {commun}")
    charlie_rare = charlie.difference(alice, bob)
    alice_rare = alice.difference(charlie, bob)
    bob_rare = bob.difference(alice, charlie)
    all_rare = charlie_rare.union(alice_rare, bob_rare)
    print(f"Rare achievements (1 player): {all_rare}\n")

    alice_bob_unique = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_bob_unique}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
