import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("Only Card instances can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0,
        }

        if not self.cards:
            return stats

        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            card_type = card.__class__.__name__

            if card_type == "CreatureCard":
                stats["creatures"] += 1
            elif card_type == "SpellCard":
                stats["spells"] += 1
            elif card_type == "ArtifactCard":
                stats["artifacts"] += 1

        stats["avg_cost"] = total_cost / len(self.cards)

        return stats
