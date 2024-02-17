day = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
current_plunder = 0
total = 0
percent = 0
for plunder in range(day):
    current_plunder = plunder * daily_plunder
    if plunder % 3 == 0:
        percent = (daily_plunder * 0.50) + current_plunder
    elif plunder % 5 == 0:
        percent = current_plunder - (daily_plunder * 0.30)
    total = current_plunder - percent
if total >= expected_plunder:
    print(f"Ahoy! {total:.2f} plunder gained.")
elif total < expected_plunder:
    print(f"Collected only {percent}% of the plunder.")
