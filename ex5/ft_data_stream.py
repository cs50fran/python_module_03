#!/usr/bin/env python3
from typing import Generator


def game_event_generator(count: int) -> Generator[dict, None, None]:
    players: list = [
            "Alice",
            "Bob",
            "Charlie",
            "Diana",
            "Eve",
            "Frank",
            "Grace",
            "Henry",
            "Ivy",
            "Jack",
            "Kate",
            "Liam",
            "Maya",
            "Noah",
            "Olivia",
            "Paul"]
    levels: list = [3, 5, 8, 12, 15, 7, 2, 11, 6, 9, 4]
    events: list = [
            "first_kill", "leveled up", "speedrun",
            "explorer", "treasure_hunter", "boss_slayer", "collector",
            "perfectionist", "social_butterfly", "lone_wolf", "strategist",
            "berserker", "pacifist", "completionist"]

    for i in range(count):
        yield {
            "player": players[i % len(players)],
            "level": levels[i % len(levels)],
            "event": events[i % len(events)]
        }


def data_stream():
    print("=== Game Data Stream Processor ===\n")

    num_of_events: int = 1000
    game_events: Generator = game_event_generator(num_of_events)

    print(f"Processing {num_of_events} game events\n")
    for i in range(1, 4):
        temp_dict = next(game_events)
        print(f"Event {i}: Player {temp_dict['player']}"
              f" (level {temp_dict['level']}) {temp_dict['event']}")
    print("...\n")

    print("=== Stream Analytics ===")
    game_events = game_event_generator(num_of_events)
    count_events: int = 0
    count_hlp: int = 0
    count_treasure: int = 0
    count_lu: int = 0
    for event in game_events:
        count_events += 1
        if event['level'] >= 10:
            count_hlp += 1
        if event['event'] == "treasure_hunter":
            count_treasure += 1
        if event['event'] == "leveled up":
            count_lu += 1

    print(f"Total events processed: {count_events}")
    print(f"High-level players (10+): {count_hlp}")
    print(f"Treasure events: {count_treasure}")
    print(f"Level-up events: {count_lu}")
    print()

    print("Memory usage: Constant (streaming)")
    print("Processing time: Very, very fast")


def fibonacci_gen() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1

    while True:
        yield a
        a, b = b, a + b


def prime_num_gen() -> Generator[int, None, None]:
    a: int = 2
    yielded: int = 0

    while True:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            yield a
            yielded += 1
        a += 1


def gen_to_list(
        gen: Generator[int, None, None],
        count: int
) -> list[int]:
    new_list: list[int] = []
    for _ in range(count):
        new_list.append(next(gen))
    return new_list


def gen_demo() -> None:
    print("\n=== Generator Demonstration ===")
    fibs_len: int = 10
    fibs = gen_to_list(fibonacci_gen(), fibs_len)

    primes_len: int = 5
    primes = gen_to_list(prime_num_gen(), primes_len)

    print(f"Fibonacci sequence (first {fibs_len}): "
          f"{', '.join(str(x) for x in fibs)}")
    print(f"Prime numbers (first {primes_len}): "
          f"{', '.join(str(x) for x in primes)}")


if __name__ == "__main__":
    data_stream()
    gen_demo()
