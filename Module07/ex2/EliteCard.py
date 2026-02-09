from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int = 0,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("attack_power must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        if not isinstance(mana_pool, int) or mana_pool < 0:
            raise ValueError("mana_pool must be a non-negative integer")

        self.attack_power: int = attack_power
        self.health: int = health
        self.mana_pool: int = mana_pool

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite creature enters play (combat + magic enabled)",
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("incoming_damage must be a non-negative integer")

        damage_taken = min(self.health, incoming_damage)
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "still_alive": self.health > 0,
            "health_left": self.health,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(spell_name, str) or not spell_name.strip():
            raise ValueError("spell_name must be a non-empty string")
        if not isinstance(targets, list):
            raise ValueError("targets must be a list")

        mana_used = min(self.mana_pool, 4)
        self.mana_pool -= mana_used

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("amount must be a non-negative integer")

        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["attack_power"] = self.attack_power
        info["health"] = self.health
        info["mana_pool"] = self.mana_pool
        return info
