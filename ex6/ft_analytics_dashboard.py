class DataBase:
    @staticmethod
    def players_scores() -> dict[str, int]:
        return {
            "Alice": 2394,
            "Bob": 234,
            "Charlie": 803,
            "Diana": 1185,
            "Eve": 2263,
            "Frank": 1175,
            "Grace": 925,
            "Henry": 1713,
            "Ivy": 1104,
            "Jack": 1011,
            "Kate": 1861,
            "Liam": 1102,
            "Maya": 2287,
            "Noah": 879,
            "Olivia": 289,
            "Paul": 1133,
        }

    @staticmethod
    def active_players() -> dict[str, bool]:
        return {
            "Alice": True,
            "Bob": False,
            "Charlie": False,
            "Diana": True,
            "Eve": False,
            "Frank": False,
            "Grace": False,
            "Henry": True,
            "Ivy": False,
            "Jack": False,
            "Kate": True,
            "Liam": True,
            "Maya": True,
            "Noah": True,
            "Olivia": False,
            "Paul": True
        }

    @staticmethod
    def players_regions() -> dict[str, str]:
        return {
            "Alice": "North",
            "Bob": "East",
            "Charlie": "South",
            "Diana": "Central",
            "Eve": "West",
            "Frank": "North",
            "Grace": "East",
            "Henry": "South",
            "Ivy": "Central",
            "Jack": "West",
            "Kate": "North",
            "Liam": "East",
            "Maya": "South",
            "Noah": "Central",
            "Olivia": "West",
            "Paul": "North"
        }

    @staticmethod
    def players_achievments() -> dict[str, list[str]]:
        return {
            "Alice": ["first_kill", "level_10", "explorer"],
            "Bob": ["level_10", "speedrun"],
            "Charlie": ["first_kill", "level_10", "level_50", "boss_slayer"],
            "Diana": ["explorer", "treasure_hunter", "collector"],
            "Eve": ["level_10", "level_50", "level_100", "perfectionist"],
            "Frank": ["speedrun", "strategist"],
            "Grace": ["lone_wolf", "pacifist"],
            "Henry": ["boss_slayer", "berserker", "completionist"],
            "Ivy": ["social_butterfly", "explorer"],
            "Jack": ["collector", "perfectionist"],
            "Kate": ["level_10", "level_50", "strategist"],
            "Liam": ["first_kill", "level_10", "level_50", "level_100"],
            "Maya": ["treasure_hunter", "boss_slayer", "collector"],
            "Noah": ["pacifist", "completionist"],
            "Olivia": ["social_butterfly"],
            "Paul": ["level_10", "speedrun", "strategist"]
        }


def combine_all_lists(dict_of_lists):
    combined = []
    for lst in dict_of_lists.values():
        combined.extend(lst)
    return combined


def get_highest_score(dict_of_ints: dict[str, int]) -> str:
    key = max(dict_of_ints, key=lambda k: dict_of_ints[k])
    return key


def game_analytics() -> None:
    print("=== Game Analytics Dashboard ===\n")

    p_scores: dict[str, int] = DataBase.players_scores()
    if not p_scores:
        print("No player scores available.")
        return

    status: dict[str, bool] = DataBase.active_players()
    if not status:
        print("No player status available.")
        return

    p_achievments: dict[str, list[str]] = DataBase.players_achievments()
    if not p_achievments:
        print("No player achievements available.")
        return

    p_regions: dict[str, str] = DataBase.players_regions()
    if not p_regions:
        print("No player regions available.")
        return

    highscores: list[str] = [n for n, s in p_scores.items() if s >= 2000]
    medscores: list[str] = [n for n, s in p_scores.items() if 1000 < s < 2000]
    lowscores: list[str] = [name for name, s in p_scores.items() if s < 1000]
    scores_cat: dict[str, int] = {
        "high": len(highscores),
        "medium": len(medscores),
        "low": len(lowscores)
    }
    double_scores: list[int] = [score * 2 for name, score in p_scores.items()]
    active_players: list[str] = [n for n, s in status.items() if s is True]
#
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {highscores}")
    print(f"Scores doubled: {double_scores}")
    print(f"Active players: {active_players}")

    all_achievments: list[str] = combine_all_lists(p_achievments)
    count_achievments: dict[str, int] = {
        key: len(value) for key, value in p_achievments.items()}
#
    print("\n=== Dict Comprehension Examples ===")
    print(f"Player Scores: {p_scores.items()}")
    print(f"Score categories: {scores_cat}")
    print(f"Achievement counts: {count_achievments}")
#
    print("\n=== Set Comprehension Examples ===")
    unik_p: set[str] = {p for p in p_scores.keys()}
    unik_a: set[str] = {a for a in all_achievments}
    active_reg: set[str] = {p_regions[p] for p in active_players}

    print(f"Unique Players: {unik_p}")
    print(f"Unique achievments: {unik_a}")
    print(f"Active regions: {active_reg}")
#
    total_p: int = len(p_scores)
    total_unik_a: int = len(unik_a)
    average_score: float = sum(p_scores.values()) / total_p
    top_player: str = get_highest_score(p_scores)
    top_score: int = p_scores[top_player]
    tp_ach_count: int = len(p_achievments.get(top_player, []))

    print("\n=== Combined Analysis ===")
    print(f"Total Players: {total_p}")
    print(f"Total unique achievments: {total_unik_a}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top Score: {top_player} ({top_score} points, "
          f"{tp_ach_count} achievments)")


def main():
    game_analytics()


if __name__ == "__main__":
    main()
