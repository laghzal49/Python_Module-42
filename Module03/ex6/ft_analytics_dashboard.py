def list_comprehension_demo(data):
    """
    Demonstrates list comprehensions for filtering and transforming data.

    Extracts:
    - Players with scores greater than 2000
    - Doubled scores from all sessions
    - Active players who played more than 20 sessions

    Args:
        data (dict): Game data containing players and sessions.
    """
    sessions = data.get('sessions', [])
    players = data.get('players', {})

    high_score = [s['player'] for s in sessions if s['score'] > 2000]
    score_doubled = [s['score'] * 2 for s in sessions]
    active_players = [n for n, p in players.items() if
                      p['sessions_played'] > 20]
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}")


def dict_comprehension_demo(data):
    """
    Demonstrates dictionary comprehensions for aggregating player statistics.

    Builds:
    - A mapping of player names to total scores
    - Player level categories (high, medium, low)
    - A mapping of player names to achievement counts

    Args:
        data (dict): Game data containing player information.
    """
    players = data.get('players', {})

    players_scores = {n: p['total_score'] for n, p in players.items()}
    score_categories = {"high": len([n for n, p in players.items() if
                                     p['level'] > 30]),
                        "medium": len([n for n, p in players.items()
                                       if 15 <= p['level'] <= 30]),
                        "low": len([n for n, p in players.items()
                                    if p['level'] < 15])}
    achievement = {n: p['achievements_count'] for n, p in players.items()}

    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement}")


def set_comprehension_demo(data):
    """
    Demonstrates set comprehensions to extract unique values.

    Extracts:
    - Unique players from sessions
    - Unique achievement names
    - Active regions from player data

    Args:
        data (dict): Game data containing players, sessions, and achievements.
    """
    players = data.get('players', {})
    achievements = data.get('achievements', [])
    sessions = data.get('sessions', [])

    unique_players = {s['player'] for s in sessions}
    unique_achievements = {a for a in achievements}
    active_regions = {a['region'] for a in players.values()}

    print(f"Unique players: {sorted(list(unique_players))}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")


def get_total_score(item):
    """
    Helper function used as a key for sorting or max selection.

    Args:
        item (tuple): A tuple of (player_name, player_info).

    Returns:
        int: The total score of the player.
    """
    return item[1]['total_score']


def all_comprehension_demo(data):
    """
    Performs combined analytics using multiple comprehension types.

    Calculates:
    - Total unique players
    - Total unique achievements
    - Average session score
    - Top-performing player by total score

    Args:
        data (dict): Complete game dataset.
    """
    players = data.get('players', {})
    sessions = data.get('sessions', [])
    achievements = data.get('achievements', [])
    total_players = len({s['player'] for s in sessions})
    total_achievements = len({a for a in achievements})

    scores = [s['score'] for s in sessions]
    avg_score = sum(scores) / len(scores) if scores else 0
    top_player, top_info = max(players.items(), key=get_total_score)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_player} ({top_info['total_score']} points,"
          f"{top_info['achievements_count']} achievements)")


def main():
    """
    Entry point of the Game Analytics Dashboard.

    Initializes sample game data and runs all
    comprehension demonstration functions.
    """
    print("=== Game Analytics Dashboard ===\n")

    data = {
        'players': {
            'alice': {'level': 41, 'total_score': 2300, 'sessions_played': 25,
                      'achievements_count': 5, 'region': 'north'},
            'bob': {'level': 16, 'total_score': 1800, 'sessions_played': 27,
                    'achievements_count': 3, 'region': 'east'},
            'charlie': {'level': 44, 'total_score': 2150,
                        'sessions_played': 21, 'achievements_count': 7,
                        'region': 'central'},
            'diana': {'level': 3, 'total_score': 2050, 'sessions_played': 5,
                      'achievements_count': 4, 'region': 'north'}
        },
        'sessions': [
            {'player': 'alice', 'score': 2300},
            {'player': 'bob', 'score': 1800},
            {'player': 'charlie', 'score': 2150},
            {'player': 'diana', 'score': 2050}
        ],
        'achievements': ['first_kill', 'level_10', 'boss_slayer']
    }

    print("=== List Comprehension Examples ===")
    list_comprehension_demo(data)
    print()
    print("=== Dict Comprehension Examples ===")
    dict_comprehension_demo(data)
    print()
    print("=== Set Comprehension Examples ===")
    set_comprehension_demo(data)
    print()
    print("=== Combined Analysis ===")
    all_comprehension_demo(data)
    print()


if __name__ == "__main__":
    main()
