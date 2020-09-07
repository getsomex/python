import random
userInput = int(input())

rock = 1
paper = 2
scissor = 3
comp = int(random.choice(['1','2','3']))
if userInput == 1:
  print('your input is rock')
  if rock == comp:
    print('computer has rock')
    print('its a tie')
  elif paper == comp:  
    print('computer has paper')
    print('you lost')
  elif scissor == comp:
    print('computer has scissor')
    print('you lost')

elif userInput == 2:
  print('your input is paper')
  if paper == comp:
    print('computer has paper')
    print('its a tie')
  elif rock == comp:
    print('computer has rock')
    print('you won')
  else:
    print('computer has scissor')
    print('you lost')
else:
  print('your input is scissor')
  if scissor == comp:
    print('computer has scissor')
    print('its a tie')
  elif paper == comp:
    print('computer has paper')
    print('you win')
  else:
    print('computer has rock')
    print('you lost')
 