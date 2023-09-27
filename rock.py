import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
  print('Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n')
  choice = int(
    input('Choice: ')
  )

  while (choice > 3 or choice < 1):
    choice = int(
      input('Enter a valid choice please ☺')
    )

  match choice:
    case 1:
      selected_user_choice = 'Rock'
    case 2:
      selected_user_choice = 'Paper'
    case 3:
      selected_user_choice = 'Scissors'

  print(f'User choice is: {selected_user_choice}\n')

  print('Now its Computers Turn....\n')

  computer_choice = random.randint(1, 3)

  match computer_choice:
    case 1:
      selected_computer_choice = 'Rock'
    case 2:
      selected_computer_choice = 'Paper'
    case 3:
      selected_computer_choice = 'Scissors'

  print(f'Computer choice is: {selected_computer_choice}\n')

  print(f'{selected_user_choice} vs {selected_computer_choice}\n')

  win_conditions = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
  }

  if win_conditions[selected_user_choice] == selected_computer_choice:
    print('User wins!')
  elif win_conditions[selected_computer_choice] == selected_user_choice:
    print('Computer wins!')
  else:
    print('It\'s a tie!')

