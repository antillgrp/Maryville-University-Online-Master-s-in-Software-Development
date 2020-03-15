from random import randint


def main():
    print("This program rolls two 6-sided dice until their sum is a given target value.")
    sumTarget = int(input("Enter the target sum to roll for: "))
    while sumTarget < 2 or sumTarget > 12:
        sumTarget = int(input("Try again. Enter the target sum to roll for(2-12): "))
    rolls = 0
    while True:
        dices = randint(1, 6), randint(1, 6)
        print("Roll: {} and {}, sum is {}".format(dices[0], dices[1], sum(dices)))
        rolls += 1
        if sum(dices) == sumTarget:
            print("Got it in {} rolls!".format(rolls))
            break


main()
