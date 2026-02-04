def main():
    """This function runs the player inventory system program."""
    print("=== Player Inventory System ===\n")

    alice = dict()
    alice["sword"] = {"type": "weapon", "rarity": "rare",
                      "quantity": 1, "price": 500}
    alice["potion"] = {"type": "consumable", "rarity": "common",
                       "quantity": 5, "price": 50}
    alice["shield"] = {"type": "armor", "rarity": "uncommon",
                       "quantity": 1, "price": 200}

    print("=== Alice's Inventory ===")
    total_value = 0
    for name, data in alice.items():
        value = data["quantity"] * data["price"]
        total_value = total_value + value
        msg1 = f"{name} ({data['type']}, {data['rarity']}): "
        msg2 = f"{data['quantity']} x @ {data['price']}"
        msg3 = f" gold each = {value} gold"
        print(msg1 + msg2 + msg3)

    print(f"\nInventory value: {total_value} gold")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")

    bob = dict()
    transfer_amount = 2

    if alice.get("potion") and alice["potion"]["quantity"] >= transfer_amount:
        alice["potion"]["quantity"] = alice["potion"]["quantity"] - 2
        bob["potion"] = {"type": "consumable", "rarity": "common",
                         "quantity": 2, "price": 50}
        print("Transaction successful!")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(f"Bob potions: {bob['potion']['quantity']}")

    print("\n=== Inventory Analytics ===")

    alice_value = 0
    for item_data in alice.values():
        alice_value = alice_value + item_data["quantity"] * item_data["price"]

    bob_value = 0
    for item_data in bob.values():
        bob_value = bob_value + item_data["quantity"] * item_data["price"]

    if alice_value >= bob_value:
        msg = f"Most valuable player: Alice {alice_value} gold"
        print(msg)
    else:
        msg = f"Most valuable player: Bob {alice_value} gold"
        print(msg)

    alice_items = 0
    for item_data in alice.values():
        alice_items = alice_items + item_data["quantity"]

    bob_items = 0
    for item_data in bob.values():
        bob_items = bob_items + item_data["quantity"]

    if alice_items >= bob_items:
        msg = "Most items: Alice (" + str(alice_items) + " items)"
        print(msg)
    else:
        msg = "Most items: Bob (" + str(bob_items) + " items)"
        print(msg)

    print("Rarest item: sword (rare)")


if __name__ == "__main__":
    main()
