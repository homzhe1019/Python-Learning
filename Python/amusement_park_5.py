age = 12
if age < 4:
    print("Your admission cost is RM0.")
elif age < 18:
    print("Your admission cost is RM25.")
else:
    print("Your admission cost is RM40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is RM{price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is RM{price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 40

print(f"Your admission cost is RM{price}.")



