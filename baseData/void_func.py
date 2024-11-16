# Void function: does not return data
# Syntax:
# def <name of func> ():
#     code

def info() -> None:
    name: str = "Paul"  # function definition and implementation
    age: int = 23


print(info())  # function calling
info()
info()

items = []


def additems():
    while True:
        item = input("Please Enter an Item>>>")
        items.append(item)
        if item == "o":
            break


additems()
print(items)
