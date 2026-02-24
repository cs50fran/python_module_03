import sys


def create_backpack() -> dict:
    total_args: int = len(sys.argv)

    if len(sys.argv) == 1:
        print("No arguments provided!")
        return None

    else:
        inventory = {}

        for i in range(1, total_args):
            item: list = sys.argv[i].split(":")
            if len(item) == 2:
                key, value = item
                try:
                    inventory[key] = int(value)
                except ValueError:
                    print(f"'{value}' is not an int()")
                    return None
            else:
                print(f"Invalid argument format: {sys.argv[i]}")
                return None

    return inventory


def see_backpack() -> None:
    backpack = create_backpack()
    if backpack is None:
        return
    total_items = sum(backpack.values())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(backpack)}")
    print()

    print("=== Current Inventory ===")
    for key, value in backpack.items():
        print(f"{key}:{value} units ({value / total_items * 100:.2f}%)")
    print()

    print("=== Inventory Statistics ===")
    max_key = None
    max_value = -9999999999
    for key, value in backpack.items():
        if value > max_value:
            max_value = value
            max_key = key

    min_key = None
    min_value = 9999999999
    for key, value in backpack.items():
        if value < min_value:
            min_value = value
            min_key = key

    print(f"Most abundant: {max_key} ({max_value} units)")
    print(f"Least abundant: {min_key} ({min_value} units)")
    print()

    print("=== Item Categories ===")

    moderate = dict()
    for key, value in backpack.items():
        if value >= 4:
            moderate[key] = value

    scarce = dict()
    for key, value in backpack.items():
        if value < 4:
            scarce[key] = value

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print()

    print("=== Management Suggestions ===")
    restock = list()
    for key, value in backpack.items():
        if value <= 1:
            restock.append(key)
    if len(restock) >= 1:
        print(f"Restock needed: {restock}")
    else:
        print("No need for restock, for now....")
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {backpack.keys()}")
    print(f"Dictionary values: {backpack.values()}")

    lookup = "sword"
    if lookup in backpack:
        print(f"Sample lookup - '{lookup}' in inventory: True")
    else:
        print(f"Sample lookup - '{lookup}' in inventory: False")


if __name__ == "__main__":
    see_backpack()
