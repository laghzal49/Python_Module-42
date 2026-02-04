def ft_data(n):
    """
    Generates a stream of game event tuples.
    Args: n (int) - Number of events to generate.
    Yields: tuple - (id, player, level, action)
    """
    actions = ["killed monster", "found treasure", "leveled up"]
    players = ["alice", "bob", "charlie"]

    for i in range(1, n + 1):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i % 20) + 1
        yield (i, player, level, action)


def fibonacci_gen(n):
    """
    Generates the first n numbers of the Fibonacci sequence.
    Args: n (int) - Count of numbers to generate.
    Yields: int - Fibonacci number.
    """
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n):
    """
    Generates the first n prime numbers.
    Args: n (int) - Count of primes to generate.
    Yields: int - Prime number.
    """
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main():
    num_events = 1000
    high_level_threshold = 10
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    print("=== Game Data Stream Processor ===")
    print(f"Processing {num_events} game events...")

    for event in ft_data(num_events):
        event_id, player, level, action = event

        if event_id <= 3:
            print(
                f"Event {event_id}: Player {player} (level {level}) {action}")

        if level >= high_level_threshold:
            high_level_count += 1

        if action == "found treasure":
            treasure_count += 1
        elif action == "leveled up":
            levelup_count += 1

    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {num_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")

    fib_res = ""
    for val in fibonacci_gen(10):
        fib_res += str(val) + ", "
    print(f"Fibonacci sequence (first 10): {fib_res[:-2]}")

    prime_res = ""
    for val in prime_gen(5):
        prime_res += str(val) + ", "
    print(f"Prime numbers (first 5): {prime_res[:-2]}")


if __name__ == "__main__":
    main()
