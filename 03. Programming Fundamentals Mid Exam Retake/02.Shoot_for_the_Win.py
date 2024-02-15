target = list(map(int, input().split(' ')))
target_counter = 0

while True:
    command = input()

    if command == 'End':
        break

    current_target = int(command)
    if current_target >= len(target):
        continue
    if target[current_target] == -1:
        continue

    for index in range(len(target)):
        if target[index] == -1:
            continue
        if index == current_target:
            continue
        elif target[index] > target[current_target]:
            target[index] -= target[current_target]
        else:
            target[index] += target[current_target]

    target[current_target] = -1
    target_counter += 1

print(f"Shot targets: {target_counter} ->", *target, sep=" ")

# first target is 0 so we reduce from 24 till all of them (24-50) (24-36) (24-70) and in the end with the first shoot
# we'v got -1, 26, 12, 46
# second shoot is invalid with 4 because the len of the target is 4, and we continue with 3 command
# the command index 3 is 46 and we add in 1 index of the target (26 + 46) = 72 and continue with target index 2 adding
# cpmmand index 3 (12 + 46) and  in target index 3 we reduce with command index (46 - 46) and is -1
#  so second shoot is -1, 72, 58, -1
# third shoot
# when is equal is always -1
# when is the target index is greater then target command index we reduce, and when the target index is less then command
# index we increase them. When the command and target index are equal the command is shoot and we need to give new
# target command

# for index in range(len(target) checking all index and if target[index] is bigger then target[current]
# we addiing them so (72 + 58) = 130 from target index "2"  58 adding target[current] "1" 72 and in target[index] is
# 130 and in target index 1 is target current 3, so tooking -1
#  and in the end will looks -1, -1, 130, -1 and after END commands its break and print shot targets: 3 and the final
# result