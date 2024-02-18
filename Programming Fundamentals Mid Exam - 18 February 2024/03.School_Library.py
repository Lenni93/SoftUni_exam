shelf = input().split("&")

while True:
    command = input()
    if command == "Done":
        break

    action, *args = command.split(" | ")

    if action == "Add Book":
        book = args[0]
        if book not in shelf:
            shelf.insert(0, book)

    elif action == "Take Book":
        book = args[0]
        if book in shelf:
            shelf.remove(book)

    elif action == "Swap Books":
        book1, book2 = args
        if book1 in shelf and book2 in shelf:
            idx1, idx2 = shelf.index(book1), shelf.index(book2)
            shelf[idx1], shelf[idx2] = shelf[idx2], shelf[idx1]

    elif action == "Insert Book":
        book = args[0]
        if book not in shelf:
            shelf.append(book)

    elif action == "Check Book":
        index = int(args[0])
        if index >= 0 and index < len(shelf):
            print(shelf[index])


print(*shelf, sep=", ")

# On the next lines until the "Done" command, you will be receiving the commands separated with " | ":
# •	"Add Book | {book name}":
# o	Add the book in the first place on the shelf.
# o	If the book is already present on the shelf, ignore the command.
# •	"Take Book | {book name}":
# o	Remove the book with the given name only if the book is on the shelf.
# o	Otherwise, ignore this command.
# •	"Swap Books | {book1} | {book2}":
# o	If both books are on the shelf, swap their places.
# o	If at least one is missing, ignore the command.
# •	"Insert Book | {book name}":
# o	Add the given book at the end of the shelf.
# o	If the book is already present on the shelf, ignore the command.
# •	"Check Book | {index}":
# o	Print the name of the book, which is at the given index.
# o	If the index is invalid, ignore the command.
