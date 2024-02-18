days = int(input())
players = int(input())
energy = float(input())
water_per_person = float(input())
food_per_person = float(input())


total_water = days * players * water_per_person
total_food = days * players * food_per_person

current_energy = energy
current_water = total_water
current_food = total_food

for day in range(1, days + 1):
    energy_loss = float(input())

    if current_energy <= 0:
        break

    if day % 2 == 0:
        water_to_drink = 0.3 * current_water
        energy_gain_from_water = 0.5 * current_energy
        current_water -= water_to_drink
        current_energy += energy_gain_from_water

    if day % 3 == 0:
        food_to_eat = current_food / players
        current_food -= food_to_eat
        energy_gain_from_food = 0.1 * current_energy
        current_energy += energy_gain_from_food

    current_energy -= energy_loss

if current_energy > 0:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")