def update_inventory(arr1, arr2):
    combined_inventory = arr1 + arr2
    inventory_dict = {}

    # Update quantities in the inventory dictionary
    for quantity, item in combined_inventory:
        inventory_dict[item] = inventory_dict.get(item, 0) + quantity

    new_inventory = []

    # Create new inventory list with updated quantities
    for item, quantity in inventory_dict.items():
        new_inventory.append([quantity, item])

    # Sort the new inventory list alphabetically by item name
    new_inventory.sort(key=lambda x: x[1])

    return new_inventory

# Example inventory lists
cur_inv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"],
]

new_inv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"],
]

updated_inventory = update_inventory(cur_inv, new_inv)
print(updated_inventory)


# def update_inventory(arr1, arr2):
    combined_inventory = arr1.copy()
    combined_inventory.extend(arr2)
    inventory_dict = {}

    # Update quantities in the inventory dictionary
    for quantity, item in combined_inventory:
        inventory_dict[item] = inventory_dict.get(item, 0) + quantity

    # Create new inventory list with updated quantities
    new_inventory = [[quantity, item] for item, quantity in inventory_dict.items()]

    # Sort the new inventory list alphabetically by item name
    new_inventory = sorted(new_inventory, key=lambda x: x[1])

    return new_inventory

# Example inventory lists
cur_inv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"],
]

new_inv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"],
]

updated_inventory = update_inventory(cur_inv, new_inv)
print(updated_inventory)
