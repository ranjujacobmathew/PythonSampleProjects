def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious forest. You can hear the sound of a river nearby.")
    print("You have a choice to make: go 'left' deeper into the forest or go 'right' towards the river.")


def forest_path():
    print("You chose to go left into the forest.")
    print("After walking for a while, you stumble upon an abandoned cabin.")
    print("Do you want to 'enter' the cabin or 'continue' deeper into the forest?")


def river_bank():
    print("You chose to go right towards the river.")
    print("You reach the river bank. You can see a small boat tied to a tree.")
    print("Will you 'take' the boat or 'explore' along the river?")


def cabin_interior():
    print("You enter the cabin and find a dusty room with a chest in the corner.")
    print("Do you want to 'open' the chest or 'leave' the cabin?")


def game_over(reason):
    print("Game Over:", reason)
    print("Would you like to play again? ('yes' or 'no')")


def main():
    introduction()

    choice1 = input().lower()

    if choice1 == 'left':
        forest_path()
        choice2 = input().lower()
        if choice2 == 'enter':
            cabin_interior()
            choice3 = input().lower()
            if choice3 == 'open':
                print("Congratulations! You found a treasure chest and won the game!")
            else:
                game_over("You left the cabin without finding anything.")
        else:
            game_over("You ventured deeper into the forest and got lost.")
    elif choice1 == 'right':
        river_bank()
        choice2 = input().lower()
        if choice2 == 'take':
            game_over("As you untied the boat, a group of wild animals approached and attacked you.")
        else:
            game_over("While exploring along the river, you fell into quicksand.")
    else:
        game_over("Invalid choice.")

    play_again = input("Do you want to play again? ('yes' or 'no') ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
