import math


def calculate_distance(pos1: tuple, pos2: tuple) -> float:
    distance: float = math.sqrt((pos1[0] - pos2[0])**2 +
                                (pos1[1] - pos2[1])**2 +
                                (pos1[2] - pos2[2])**2)
    return (f"Distance between {pos1} and {pos2}: {distance:.2f}")


def coordinates_sys():
    print("=== Game Coordinate System ===\n")
    start_pos: tuple = (0, 0, 0)

    pos1: tuple = (10, 20, 5)
    print(f"Position Created: {pos1}")
    print(calculate_distance(start_pos, pos1))
    print()

    """ Parsing valid coordinates"""
    str_pos2: str = "3,4,0"
    pos2: tuple = tuple(int(x) for x in (str_pos2.split(",")))
    print(f"Parsing coordinates: \"{str_pos2}\"")
    print(f"Parsed position: {pos2}")
    print(calculate_distance(start_pos, pos2))
    print()

    """ Parsing invalid coordinates """
    str_pos3: str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{str_pos3}"')
    try:
        tuple(int(x) for x in str_pos3.split(","))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")

    """ Unpacking Tuples """
    x, y, z = pos2
    print("Unpacking Demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinates_sys()
