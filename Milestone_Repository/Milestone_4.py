
### Create the Class.

import random
word_list = ["one","two","three","four","five"]
word = random.choice(word_list)
word_guessed = ['_' for _ in word]
guess_list = [""]
num_letters = len(set(word_guessed))
guess = input("Enter a letter: ").lower() 


class Hangman:
   def __init__(self):
       self.word = word
       self.word_guessed = ['_' for _ in self.word]
       self.num_letters = len(set(self.word))
       self.word_list = word_list
       self.num_lives = 3
       self.guess_list = guess_list
  
### Create methods for running the checks.
### Define what happens when the letter is in the chosen word.
### Define what happens when the letter is NOT in the chosen word.

   def check_guess(self, guess):
        global word_guessed, num_letters
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    word_guessed = word_guessed[:i] + [guess] + word_guessed[i+1:]
            self.num_letters -= 1
            print ("Letters remaining", self.num_letters)
        else:
            print("Sorry,",guess,"is not in the word")
            self.num_lives -= 1
            print("You have",self.num_lives,"lives left.")
        print(word_guessed)
        print(self.num_letters)

   def ask_for_input(self):
        while True:
            if len(guess) != 1 or not guess.isalpha():
             return print("Invalid input. Please enter a single alphabetical character.")
            elif guess in self.guess_list:
             return print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.guess_list.append(guess)
                break


hangman_game = Hangman()
hangman_game.ask_for_input()
