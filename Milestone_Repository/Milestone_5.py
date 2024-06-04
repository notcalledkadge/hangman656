
import random

word_list = ["black","dumbledore","hagrid","lupin","malfoy","mcgonagall","potter","snape","weasley","flitwick","sprout","wood","dursley","brown","chang","crabbe","goyle","fudge","lestrange","moody","filch","crouch"]
word = random.choice(word_list)
word_guessed = ['_' for _ in word]
guess_list = [""]
num_letters = len(set(word_guessed))
num_lives = 5

class Hangman:
   def __init__(self):
       self.word = word
       self.word_guessed = ['_' for _ in self.word]
       self.num_letters = len(set(self.word))
       self.word_list = word_list
       self.num_lives = num_lives
       self.guess_list = guess_list

   def check_guess(self, guess):
        global word_guessed, num_letters
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    word_guessed = word_guessed[:letter] + [guess] + word_guessed[letter+1:]
            self.num_letters -= 1
            print ("Letters remaining", self.num_letters)
        else:
            print("Sorry,",guess,"is not in the word")
            self.num_lives -= 1
            if self.num_lives >1:
             print("You have",self.num_lives,"lives left.")
            if self.num_lives ==1:
             print("You have",self.num_lives,"life left.")
        print(word_guessed)


   def ask_for_input(self):
        guess = input("Enter a letter: ").lower() 
        while True:
            if len(guess) != 1 or not guess.isalpha():
             return print("Invalid input. Please enter a single alphabetical character.")
             
            elif guess in self.guess_list:
             return print("You already tried that letter!")
             
            else:
                self.check_guess(guess)
                self.guess_list.append(guess)
                break

### Code the logic of the game.

def play_game():
    print(word_guessed)
    game = Hangman()
    while True:
         if game.num_lives == 0:
          print ("You lost! The word was:",word)
          break
         elif game.num_letters > 0:
          game.ask_for_input() 
         else:
          print("Congratulations! You win! The word was:",word)
          break

play_game()
                   
       