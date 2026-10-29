menu = {"apple": 0.5,
         "banana": 0.25,
           "orange": 0.75}
cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    item = input("Item: ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)
        for item in cart:
            total += menu.get(item)
            print(item, end=" " )

print()
print(f"Total: ${total:.2f}")
    