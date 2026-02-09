from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        if not self._validate_effect_type():
            raise ValueError(
                "Effect type must be one of: damage, heal, buff, debuff")

    def _validate_effect_type(self) -> bool:
        allowed = {"damage", "heal", "buff", "debuff"}
        return self.effect_type in allowed

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Spell cast: {self.effect_type}",
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
