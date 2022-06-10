import random

alist = ['"R" for rock, "P" for paper, "S" for scissors"']
for item in alist:
    print(item)

#take user input
while True:
    user_choice = input('Enter a choice(R, P, S): ')
    user_choice = user_choice.upper()
    possible_actions = ['rock', 'paper', 'scissors']
    type_of_user_choice = type(user_choice) 
    choice_name = ' '
    if user_choice == 'R':
        choice_name = 'Rock'
    elif user_choice == 'P':
        choice_name = 'Paper'
    elif user_choice == 'S':
        choice_name = 'Scissors'
    else:
        print('Error! Enter a valid choice')
        continue
    print('user choice is: ' + choice_name)
    print('\nNow its computer turn.......')
    comp_action = random.choice(possible_actions)
    print(f'\nYou chose {choice_name}, computer chose {comp_action}.\n')

    if user_choice == comp_action:
        print(f'Both players selected {user_choice}. Its a tie!')
    elif user_choice == 'R':
        if comp_action == 'scissors':
            print('Rock beats scissors! You win!')
        else:
            print('paper beats rock! You lose.')
    elif user_choice == 'P':
        if comp_action == 'rock':
            print('Paper beats rock! You win!')
        else:
            print('Scissors beats rock! You lose.')
    elif user_choice == 'S':
        if comp_action == 'paper':
            print('Scissors beats paper! You lose.')
        else:
            print('Rock beats scissors! You lose.')
    play_again = input('Do you want to play again? (y/n): ')
    if play_again.lower() != 'y':
        break
            
    
    



    
    
