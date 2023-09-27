import random

def _catNames():
  catNames = []

  while True:
    catNumber = str(len(catNames) + 1)
    print('Enter the name of the cat ' + catNumber + ' (Or enter nothing to stop.)')
    name = input()

    if (name == ''):
      break  
    catNames = catNames + [name] # concatenation

  print('The cat names are:')
  for name in catNames:
    print(' ' + name)

def _magic8Ball():
  messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
  ]
  print(messages[random.randint(0, len(messages) - 1)])

def _dictonary():
  birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

  while True:
    print('Enter a name: (blank to quit)')
    name = input()

    if (name == ''):
      break

    if name in birthdays:
      print(birthdays[name] + ' is the birthday of ' + name)
    else:
      print('I do not have birthday information for ' + name)
      print('What is their birthday?')

      bday = input()
      birthdays[name] = bday
      print('Birthday database updated.')

_dictonary()
