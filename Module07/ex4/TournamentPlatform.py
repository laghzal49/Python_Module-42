from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registered_cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.lower()}_{len(self.registered_cards) + 1}"
        self.registered_cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        card1.attack(card2)

        if card2.health <= 0:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1
        winner.update_wins(1)
        loser.update_losses(1)
        winner.rating = winner.calculate_rating()
        loser.rating = loser.calculate_rating()

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        leader = sorted(self.registered_cards.values(),
                        key=lambda card: card.rating, reverse=True)
        return [card.get_tournament_stats() for card in leader]

    def generate_tournament_report(self) -> dict:
        total = len(self.registered_cards)

        if total > 0:
            avg = sum(
                card.rating for card in self.registered_cards.values()) / total
        else:
            avg = 0
        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }
