def menu():
    print(
        """
1. Show file content
2. Add item, append
3. Replace content
4. Remove an item
        """
        )
    return int(input("Choice: "))

def readfile():
    with open("items.txt") as fhand:
        content = fhand.read()
    return content

def writefile(item, mode):
    with open('items.txt', mode) as fhand:
        fhand.write(item)

def replace_content():
    item = ""
    result = ""
    while item != "q":
        result += item + "\n"
        item = input("Item to add: ")
    writefile(result, "w")

def choice(inp):
    if inp == 1:
        print(readfile())
    elif inp == 2:
        writefile("\n" + input("What do you wanna append to file?: "), "a")
    elif inp == 3:
        replace_content()
    elif inp == 4:
        pass
    else:
        exit()

if __name__ == "__main__":
    while(True):
        choice(menu())