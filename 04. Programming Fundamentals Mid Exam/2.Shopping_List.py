
initial_list_with_groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command_part = command.split()
    action = command_part[0]

    if action == "Urgent":
        item1 = command_part[1]


        if item1 not in initial_list_with_groceries:
            initial_list_with_groceries.insert(0, item1)

    elif action == "Unnecessary":
        item1 = command_part[1]
        if item1 in initial_list_with_groceries:
            initial_list_with_groceries.remove(item1)

    elif action == "Correct":
        old_item = command_part[1]
        new_item = command_part[2]
        if old_item in initial_list_with_groceries:
            old_item_index = initial_list_with_groceries.index(old_item)
            initial_list_with_groceries[old_item_index] = new_item
    elif action == "Rearrange":
        item1 = command_part[1]
        if item1 in initial_list_with_groceries:
            initial_list_with_groceries.remove(item1)
            initial_list_with_groceries.append(item1)

print(*initial_list_with_groceries, sep=", ")
