import random
print('choose any of the following bellow')
print('1. ✊ rock')
print('2. ✋ paper')
print('3. ✌️ scissor')
player = int(input('pick a number between 1 to 3: '))
if player == 1:
  print('you chose this: ✊')
elif player == 2:
  print('you chose this: ✋ ')
elif player == 3:
  print('you chose this: ✌️')
else:
  print('choose the numbers only between 1 and 3')
computer = random.randint(1,3)
if computer == 1:
  print('cpu chose this: ✊')
elif computer == 2:
  print('cpu chose this: ✋ ')
else:
  print('cpu chose this: ✌️')
if player == computer:
     print("It's a tie!")
elif (player == '✊' and computer == '✌️') or \
     (player == '✋' and computer == '✊') or \
     (player == '✌️' and computer == '✋'):
      print("You win!")
else:
     print("You lose!")



