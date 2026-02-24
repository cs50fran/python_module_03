def tracker():
    alice = {'first_kill',
             'level_10',
             'treasure_hunter',
             'speed_demon'}
    bob = {'first_kill',
           'level_10',
           'boss_slayer',
           'collector'}
    charlie = {'level_10',
               'treasure_hunter',
               'boss_slayer',
               'speed_demon',
               'perfectionist'}

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print()

    common = alice & bob & charlie

    unique_alice = alice - bob - charlie
    unique_bob = bob - alice - charlie
    unique_charlie = charlie - bob - alice
    unique = unique_alice | unique_bob | unique_charlie

    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {unique}")
    print()

    """ Alice vs Bob"""
    print(f"Alice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    tracker()
