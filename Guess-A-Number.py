import random

while True:
    computer_number = random.randint(1,100)
    tries = 0

    while True:
        player_input = input('Try to guess the number that the computer has picked between 1 - 100: ')
        if not player_input.isdigit():
            print('Invalid choice. Please try again.')
            continue

        player_choice = int(player_input)

        if player_choice == computer_number:
            print('You guessed right! Congratulations!')
            tries = 0
            break

        elif player_choice > computer_number:
            print('Guess is too high!')


        else:
            print(f'Guess is too low!')

        tries += 1
        if tries == 10:
            print("Sorry! You couldn't guess the number")
            break

    a = input('Do you want to play again? (y/n): ')
    while a != 'y' or a != 'n':
        if a == 'y':
            print('The computer has picked a new number. Try to guess it.')
            break
        elif a == 'n':
            print('GG')
            exit()
        else:
            a = input('Invalid choise\nPick (y/n): ')
