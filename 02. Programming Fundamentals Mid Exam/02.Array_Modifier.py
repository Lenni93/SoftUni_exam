array_value = [int(number) for number in input().split()]
command = input().split(" ")
while command[0] != "end":
    action = command[0]
    if action == 'swap':
        first_index, second_index = int(command[1]), int(command[2])
        array_value[first_index], array_value[second_index] = array_value[second_index], array_value[first_index]
    elif action == 'multiply':
        first_index, second_index = int(command[1]), int(command[2])
        array_value[first_index] *= array_value[second_index]
    elif action == 'decrease':
        array_value = [number - 1 for number in array_value]
    command = input().split()
print(*array_value, sep=", ")


#array_value = [list(map(int, input().split(" ")))]
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     if command == 'decrease':
#         for element in range(len(array_value)):
#             array_value[element] -= 1
#         continue
#     indexes = command.split(" ")
#     index1 = int(indexes[1])
#     index2 = int(indexes[2])
#     if indexes[0] == 'swap':
#         array_value[index1], array_value[index2] = array_value[index2], array_value[index1]
#     if indexes[0] == 'multiply':
#         array_value[index1] *= array_value[index2]
#
# print(*array_value, sep=", ")
#indexes split the command by 3 and indicated with 3 indexes, swap index is indicated in indexes, 1st index is indicated
#in index1, and second index is indicated in index2
#in the swapping array is 1st index -2 and 87, so they will change the position as