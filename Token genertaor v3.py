import random


tokens = ["unicorn", "horse", "horse", "horse", "Zebra", "zebra", "zebra", "donkey", "donkey," "donkey"]
starting_balance = 100

balance = starting_balance

for item in range (0,100):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5


print()
print("Starting balance: ${}" .format (starting_balance))
print("Final balanced: ${}" .format(balance))
