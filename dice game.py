import random
roll = True
while roll:
    choice = input("enter your choice want to roll the dice yes/no:")
    if choice == 'yes':
        print("rolling the dice.....")
        print("wait for it..")
        n = (random.randint(0,6))
        print(n)
        roll = True
    else:
        print("thankyou for using the dice")
        roll = False