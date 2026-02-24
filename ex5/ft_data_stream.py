#!/usr/bin/env python3
from typing import Generator


def game_event_generator(count: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie", "diana", "eve"]
    events  = ["killed monster", "found treasure", "leveled up"]
    levels  = [3, 5, 8, 12, 15, 7, 2, 11, 6, 9]

    for i in range(count):
        yield {
            "player": players[i % len(players)],
            "level": 5,
            "event": "killed monster"
        }

def data_stream():
    print("=== Game Data Stream Processor ===\n")

    events = Generator()

    print("Processing 1000 game events...\n")

    