import random 

def word_list():
   fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
   print(fruits)
# word_list()

def word():
   fruits = ["banana", "strawberry", "orange", "apples", "kiwi"]
   random_fruit = random.choice(fruits)
   print(random_fruit)
# word()

def guess():
   letter = input("Please only input a single letter:").lower()
   #print(len(letter))
   #if len(letter) == 1 and isinstance(letter, str):
   if len(letter) ==1 and letter.isalpha():
    # return print("Ooh, that's the right length")
    return print("Good guess!")
    # elif len(letter) > 1 or type(letter) == int:
   else:
    return print("Oops! That is not a valid input.")
guess()
   
   