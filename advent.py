name = input("type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to and end you can go left or right which way would like to?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk or swim to swim across: ")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross or head back? ")

    if answer == "back":
        print("You walked back and fell, so you lost bootyhead!")
    
    elif answer == "cross":
        answer = input("You cross the bridge and met a stranger, do you want to talk to them Yes or No?")

        if answer == "Yes":
            print("You talked to the stranger and they gave you tesla now drive back home YOU WON!")
        elif answer == "No":
            print("You ignored the stranger and he shot you in the head and you died!")
        else:
            print('Not a valid option you lose.')

else:
    print('Not a valid option. You lose')

print("Thank you for trying", name)




