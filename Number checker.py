error = "Please enter an whole number between 1 and 10"

vaild = False
while not vaild:

     Response = int(input("How much would you like to play with?"))

if 0 < response  <= 10:
    print("You have to asked to play with ${}" .format(response))

else:
    print(Error)
