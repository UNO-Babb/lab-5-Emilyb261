#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""

    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""

    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""

    for i in range(len(myGuess)):
     letter= myGuess[i]
    if inSpot(letter, word, i):
     result += letter.upper()
    elif inWord(letter, word):    
      result += letter.lower()
    else:
        result =+ "*"

    return result 

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    for attempt in range(1, 7):
        guess = input(f"Guess {attempt}/6: ").strip().lower()

        # check length match
        if len(guess) != len(todayWord):
            print(f"Your guess must be {len(todayWord)} letters long.")
            continue

        feedback = rateGuess(guess, todayWord)
        print("Feedback:", feedback)

        if guess == todayWord:
            print(f" You guessed it in {attempt} tries!")
            break
    else:
        print("Out of guesses :( The word was:", todayWord)


    #Ask user for their guess
    #Give feedback using on their word:

if __name__ == '__main__':
  main()
