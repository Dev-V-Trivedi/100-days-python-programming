# Affirmation Generator By dev

print('Wholesome Positivity Machine')


name = input('What is your name? ')

achieve = input('What do you want to achieve? ')

scale = input("On a scale of 1-10, how are you feeling today? (1 being the worst, 10 being the best) ")

if scale == '1':
  print(name + ', every step you take brings you closer to achieving ' + achieve + '!')
elif scale == '2':
  print(name + ', you are stronger than any challenge standing between you and ' + achieve + '.')
elif scale == '3':
  print('Your efforts are creating magic, ' + name + ', and soon you\'ll achieve ' + achieve + '!')
elif scale == '4':
  print('Even on tough days, ' + name + ', you are growing and getting closer to ' + achieve + '.')
elif scale == '5':
  print(name + ', your inner light is guiding you toward the success of ' + achieve + '.')
elif scale == '6':
  print('Feeling low today doesn\'t change the fact, ' + name + ', that you are destined to achieve ' + achieve + '.')
elif scale == '7':
  print(name + ', it\'s okay to rest — your dream of ' + achieve + ' is still alive and waiting for you.')
elif scale == '8':
  print('The universe is working in your favor, ' + name + ', to help you achieve ' + achieve + '.')
elif scale == '9':
  print(name + ', you have conquered every bad day so far — and you\'re powerful enough to achieve ' + achieve + ' too!')
elif scale == '10':
  print(name + ', you are loved, appreciated, and on your way to achieving ' + achieve + '.')
else:
  print('Please enter a valid number between 1 and 10.')

print('Thank you for using the Wholesome Positivity Machine!')
print('Have a great day!')