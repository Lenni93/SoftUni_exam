route = input().split("||")
fuel = int(input())
ammunition = int(input())
for command in route:
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    command_part = command.split()
    command_type = command_part[0]
    value = command_part[1]

    if command_type == "Travel":
        distance = int(value)
        if fuel >= distance:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif command_type == "Enemy":
        enemy_armor = int(value)
        if ammunition >= enemy_armor:
            ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        else:
            fuel_needed_to_escape = 2 * enemy_armor
            if fuel >= fuel_needed_to_escape:
                fuel -= fuel_needed_to_escape
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif command_type == "Repair":
        ammo_added = int(value) * 2
        fuel_added = int(value)
        ammunition += ammo_added
        fuel += fuel_added
        print(f"Ammunitions added: {ammo_added}.")
        print(f"Fuel added: {fuel_added}.")


