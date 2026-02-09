from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.rating = 1200
        self.wins = 0
        self.losses = 0

    def get_tournament_stats(self) -> dict:
        stats = self.get_rank_info()
        stats["card_name"] = self.name
        return stats

    def attack(self, target) -> dict:
        target_response = target.defend(self.attack_power)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee",
            "target_result": target_response
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
            "health": self.health
        }

    def calculate_rating(self) -> int:
        rate = ((self.wins * 1000) - (self.losses * 500))
        return rate

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "current_rating": self.rating,
            "total_wins": self.wins,
            "total_losses": self.losses
        }

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "cost": getattr(self, 'cost', 0),
            "effect": f"{self.name} enters the tournament arena!"
        }
