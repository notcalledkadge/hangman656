import random 

### Define the list of possible words.
def word_list():
   fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
   print(fruits)
# word_list()

### Choose a random word from the list.
def word():
   fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
   random_fruit = random.choice(fruits)
   print(random_fruit)
# word()

### Ask the user for an input.
def guess():
   letter = input("Please only input a single letter:").lower()
   #print(len(letter))
   #if len(letter) == 1 and isinstance(letter, str):

### Check that the input is a single character.
   if len(letter) ==1 and letter.isalpha():
    # return print("Ooh, that's the right length")
    return print("Good guess!")
    # elif len(letter) > 1 or type(letter) == int:
   else:
    return print("Oops! That is not a valid input.")
guess()
   
   