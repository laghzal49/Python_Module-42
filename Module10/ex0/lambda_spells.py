from typing import Dict


def artifact_sorter(artifacts: list[Dict]) -> list[Dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[Dict], min_power: int) -> list[Dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[Dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]
    avg_power = sum(map(lambda m: m["power"], mages)) / len(mages)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": round(avg_power, 2)
    }


def main():
    try:
        print("\nTesting artifact sorter...")
        artifacts = [
            {"name": "Fire Staff", "power": 92},
            {"name": "Cloak of Invisibility", "power": 70},
            {"name": " Crystal Orb", "power": 85},
        ]
        sorted_artifacts = artifact_sorter(artifacts)
        print(f"{sorted_artifacts[0]['name']}"
              f" ({sorted_artifacts[0]['power']} power) come before"
              f" {sorted_artifacts[1]['name']} "
              f"({sorted_artifacts[1]['power']} power)\n")
        print("\nTesting spell transformer...")
        spells = ["Fireball", "heal", "shield"]
        new_spells = spell_transformer(spells)
        for spell in new_spells:
            print(spell, end=' ')
        print()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
