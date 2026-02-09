from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    platfrom = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 8, 10)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 6)
    print("Registering Tournament Cards...")
    dargon_id = platfrom.register_card(dragon)
    wizard_id = platfrom.register_card(wizard)
    print(f"{dragon.name} registered with ID: {dargon_id}")
    print(f"{wizard.name} registered with ID: {wizard_id}")
    print("\nCreating tournament match...")
    match_result = platfrom.create_match(dargon_id, wizard_id)
    print(f"Match result: {match_result}")
    leaderboard = platfrom.get_leaderboard()
    for i, card_stats in enumerate(leaderboard, 1):
        print(f"{i}. {card_stats['card_name']} - Rating: "
              f"{card_stats['current_rating']} "
              f"({card_stats['total_wins']}-{card_stats['total_losses']})")
    print("\nPlatform Report:")
    report = platfrom.generate_tournament_report()
    print(report)
    print("=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    main()
