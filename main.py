import random
pc=random.choice("swg")
print("Greetings Player! ")
print("Choose from Snake, Water, or Gun")
print("To choose u must use the first letter of your choice in lowercase:")
print("LEts Start the game! ")
a=input("Enter your Choice Player:  ")
if(a==pc):
    print(f"Dumbass! Its a Draw")
elif(a=="s" and pc=="w"):
    print("Chii,You won")
elif(a=="w" and pc=="g"):
    print("You won,😑")
elif(a=="g" and pc=="s"):
    print("You won,🤮")
elif(pc=="w"and a=="g"):
    print("I won🥱")
elif(pc=="s"and a=="w"):
    print("I won👾")
elif(pc=="g"and a=="s"):
    print("I won")