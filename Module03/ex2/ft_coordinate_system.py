import math


def calculate_distance(p1, p2):
    """
    Calculates 3D Euclidean distance between two tuples.
    Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def main():
    """Testing with Running all Tests Here and
    Parse the All Corddinate """
    print("=== Game Coordinate System ===\n")

    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")

    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {round(dist1, 2)}\n")

    input_str = "3,4,0"
    print(f'Parsing coordinates: "{input_str}"')

    try:
        parts = input_str.split(',')
        pos2 = (int(parts[0]), int(parts[1]), int(parts[2]))
        print(f"Parsed position: {pos2}")

        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2}\n")

    except Exception as e:
        print(f"Unexpected error: {e}")

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')

    try:
        parts = invalid_str.split(',')
        invalid_pos = (int(parts[0]), int(parts[1]), int(parts[2]))
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")

    print("Unpacking demonstration:")
    if 'pos2' in locals():
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
