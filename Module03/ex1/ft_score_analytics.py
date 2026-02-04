import sys


def main():
    """
    Process command-line scores and display statistical analytics.
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <s1> <s2> ...")
        return

    mylist = []
    try:
        for i in range(1, len(sys.argv)):
            mylist.append(int(sys.argv[i]))
    except ValueError:
        print("Error: All scores must be integers.")
        return

    count = len(mylist)
    if count == 0:
        return

    total_score = sum(mylist)
    avg_score = total_score / count
    high_score = max(mylist)
    low_score = min(mylist)

    print(f"Scores processed: {mylist}")
    print(f"Total players: {count}")
    print(f"Total score: {total_score}")
    print(f"Average score: {avg_score:.2f}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
