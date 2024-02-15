total_price = 0
taxes = 0
price_without_taxes = 0
while True:
    computer_price = input()

    if computer_price == 'special' or computer_price == 'regular':
       break

    computer_price = float(computer_price)

    if computer_price < 0:
        print("Invalid price!")
        continue
    total_price += computer_price
    price_without_taxes += computer_price
    taxes += computer_price * 0.20

total_price += taxes
if computer_price == 'special':
    total_price *= 0.90
if total_price == 0:
    print('Invalid order!')
if total_price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f'Taxes: {taxes:.2f}$')
    print("-----------")
    print(f"Total price: {total_price:.2f}$")