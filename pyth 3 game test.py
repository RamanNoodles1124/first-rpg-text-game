
answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = input("you reach a crossroads, would you like to go left or right").lower().strip()
    if answer == "left":
        answer = input("you encounter a monster, would you like to run or attack.")

        if answer == "attack":
            print("You lost that was really stupid why would u fight a monster")
        else:
           print("Good choice dont fight monsters")

           answer = input("would you say you enjoyed this game? (yes/no)")

           if answer == "yes":
                print("aww thank you ;-;")
           else:
                print("go away then")


    elif answer == "right":
        print("you walk aimlessly to the right and fall on a patch of ice. You injure your leg and cannot continue. Game over!")

else: 
    print("go away")
