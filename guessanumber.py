# Fancy-pants recursive solution:
def int_input():
  guessed_number_string = raw_input("Guess a number: ")  
  try:
      guessed_number = int(guessed_number_string)
  except:
      print "I need an integer...Try again"
      guessed_number = int_input()
  assert type(guessed_number) == type(1)
  return guessed_number

# Pedestrian version:
def int_input():
  while True:
    guessed_number_string = raw_input("Guess a number: ")  
    try:
      guessed_number = int(guessed_number_string)
      return guessed_number
    except:
      print "I need an integer...Try again"
      
    














while True:
#  number_to_guess = 321
  import random
  number_to_guess = random.randint(1,999)

  number_of_loops = 0

  while number_of_loops < 20:
    guessed_number = int_input()
    
    if guessed_number == number_to_guess:
      print "snag it"
      break

     
    if guessed_number >= number_to_guess:
      print "too high"

    if guessed_number <= number_to_guess:
      print "too low"
  
    number_of_loops = number_of_loops + 1

  print "Thank you for playing"
