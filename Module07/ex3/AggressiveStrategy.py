from typing import Any, Dict, List

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Aggressive strategy:
    - Play creatures first, then spells, then artifacts
    - Play lowest-cost cards first until mana runs out
    - Attack the enemy player directly
    """

    def __init__(self, starting_mana: int = 6) -> None:
        self.starting_mana = starting_mana

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        if not available_targets:
            return []
        strings = [t for t in available_targets if isinstance(t, str)]
        others = [t for t in available_targets if not isinstance(t, str)]
        strings.sort(
            key=lambda s: 0 if s.lower() in ("enemy player", "player") else 1
        )
        return strings + others

    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:

        available_mana = self.starting_mana
        type_rank = {"Creature": 0, "Spell": 1, "Artifact": 2}

        def _info(card: Any) -> dict:
            return getattr(card, "get_card_info", lambda: {})()

        def _cost(card: Any) -> int:
            c = _info(card).get("cost", 999999)
            return int(c) if isinstance(c, int) else 999999

        def _type(card: Any) -> str:
            return str(_info(card).get("type", ""))

        # --- Sort hand: creatures first, then by cost ---
        hand_sorted = sorted(
            hand,
            key=lambda c: (type_rank.get(_type(c), 99), _cost(c))
        )

        cards_played: List[str] = []
        remaining_hand: List[Any] = []
        mana_used = 0
        damage_dealt = 0

        # --- Phase 1: Play cards ---
        for card in hand_sorted:
            if not hasattr(card, "is_playable") or not hasattr(card, "play"):
                remaining_hand.append(card)
                continue

            if card.is_playable(available_mana):
                result = card.play({"available_mana": available_mana})

                name = result.get("card_played", str(card))
                cards_played.append(name)

                spent = int(result.get("mana_used", 0))
                mana_used += spent
                available_mana -= spent

                damage_dealt += int(result.get("damage", 0))

                if _type(card) == "Creature":
                    battlefield.append(card)
            else:
                remaining_hand.append(card)

        # --- Phase 2: Attack with all creatures ---
        targets = self.prioritize_targets(["Enemy Player"])
        targets_attacked: List[str] = []

        if targets:
            target_name = str(targets[0])

            for creature in battlefield:
                if hasattr(creature, "attack_target"):
                    res = creature.attack_target(target_name)
                    targets_attacked.append(target_name)
                    dmg = res.get("damage_dealt", 0)
                    if isinstance(dmg, int):
                        damage_dealt += dmg

                elif hasattr(creature, "attack"):
                    res = creature.attack(target_name)
                    targets_attacked.append(target_name)
                    dmg = res.get("damage", 0)
                    if isinstance(dmg, int):
                        damage_dealt += dmg

        return {
            "strategy": self.get_strategy_name(),
            "hand_size_start": len(hand),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets_attacked,
                "damage_dealt": damage_dealt,
            },
            "hand_size_end": len(remaining_hand),
            "battlefield_size_end": len(battlefield),
        }
