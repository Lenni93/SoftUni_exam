day = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
current_plunder = 0
total_plunder = 0
for plunder in range(1, day + 1):
    total_plunder += daily_plunder

    if plunder % 3 == 0:
        total_plunder += 0.50 * daily_plunder
    elif plunder % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
elif total_plunder < expected_plunder:
    percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
