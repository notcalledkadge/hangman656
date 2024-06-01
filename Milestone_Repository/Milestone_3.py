import random 

# def word_list():
#    fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
#    print(fruits)
# # word_list()

# def word():
#    fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
#    random_fruit = random.choice(fruits)
#    print(random_fruit)
# # word()

def guess():
 while True:
  letter = input("").lower()
  if len(letter) ==1 and letter.isalpha():
   return letter
  else:
   print("Invalid letter. Please, enter a single alphabetical character.")
# guess()

def letter_checker():
  fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
  random_fruit = random.choice(fruits)
#   print(random_fruit)
  letter = input("")

  if letter in random_fruit:
   print("good guess!" ,letter, "is in the word!")
  else:
   print("Sorry!" ,letter, "was not in the word. What a bummer!")
# letter_checker()

 
# def letter_checker():
#   fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
# #   print(random_fruit)
#   letter = input("")

def check_guess():
  checked_letter = guess().lower()
  fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
  random_fruit = random.choice(fruits)
  if checked_letter in random_fruit:
   print("good guess!" ,checked_letter, "is in the word!")
  else:
   print("Sorry!" ,checked_letter, "was not in the word. What a bummer!")
# check_guess()

def ask_for_input():
 check_guess()
 while True:
  letter = input("").lower()
  if len(letter) ==1 and letter.isalpha():
   return letter
  else:
   print("Invalid letter. Please, enter a single alphabetical character.")
# ask_for_input()