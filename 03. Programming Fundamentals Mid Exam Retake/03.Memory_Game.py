from math import floor

element = input().split(' ')
number_of_moves = 0
while True:
    command = input()
    if command == 'end':
        break
    if len(element) < 2:
        continue
    number_of_moves += 1
    indexes = command.split(' ')
    first_index = indexes[0]
    second_index = indexes[1]
    first_index = int(first_index)
    second_index = int(second_index)
    if first_index == second_index or first_index < 0 or second_index < 0 or first_index > len(element) - 1 \
       or second_index > len(element) - 1:
        middle_element = len(element) / 2
        middle_element = floor(middle_element)
        element.insert(middle_element, f'-{number_of_moves}a')
        element.insert(middle_element, f'-{number_of_moves}a')
        print('Invalid input! Adding additional elements to the board')
        continue
    elif element[first_index] == element[second_index]:
        print(f'Congrats! You have found matching elements - {element[first_index]}!')
        if second_index > 0:
            second_index -= 1
        element.pop(first_index)
        element.pop(second_index)
        continue
    else:
        print('Try again!')
        continue

if len(element) < 2:
    print(f'You have won in {number_of_moves} turns!')
else:
    print("Sorry you lose :(")
    print(*element)