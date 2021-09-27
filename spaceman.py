import random

guessed_secret_word = []

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for i in guessed_secret_word:
        if i == "_":
            return False
    else:
        return True

def get_guessed_word(secret_word, letters_guessed):
    i = 0
    wordLength = len(secret_word)
    while i < wordLength:
        guessed_secret_word.append("_")
        i += 1
    return True


def is_guess_in_word(guess, secret_word):
    i = 0
    included = 0
    for letter in secret_word:
        if guess == letter:
            guessed_secret_word[i] = str(guess)
            included += 1    
        i += 1
    if included == 0:
        return False
    else:
        return True

def spaceman(secret_word):
    missedGuesses = 0
    guesses = 0
    guessed_letters = []

    print("----------------- WELCOME TO SPACEMAN --------------------")
    print("Welcome to Spaceman. A new and epic guessing game.")
    print('')
    print("--------------------- INSTRUCTIONS -----------------------")
    print("How it works is simple. There is a word you are trying to guess.")
    print("You will be guessing letters that you think are in the secret word")
    print("If you guess a letter in the word, it will fill in the blank.")
    print("You will have 7 guess attempts to figure out the secret word of you will lose.")
    print("")
    print("------------------- LETS GET STARTED --------------------")
    print("Are you read to start the game!")
    startGame = input("Are you ready to start the game [Y/N]: ")

    if startGame == "N":
        print("Thanks for playing. Hope to see you soon.")
    if startGame == "Y":
        get_guessed_word(secret_word, guessed_letters)
        while missedGuesses < 7:
            guessesLeft = 7 - missedGuesses
            print(guessed_secret_word)
            guessed_letter = input(F'You have {guessesLeft} guesses left! Guess a letter: ')
            guessed_letters.append(guessed_letter)
            guessedCorrectly = is_guess_in_word(guessed_letter, secret_word)
            if guessedCorrectly == False:
                missedGuesses += 1
            if guessedCorrectly == True:
                missedGuesses += 0
            correctlyGuessedWord = is_word_guessed(secret_word, guessed_letters)
            if correctlyGuessedWord == True:
                print("Congrats on guessing the word")
                break
        if missedGuesses == 7:
            print("Sorry you ran out of guesses. Better luck next time!")

secret_word = load_word()
print(secret_word)
spaceman(secret_word)