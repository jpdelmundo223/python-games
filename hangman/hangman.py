import random
import os

chances = 4
words = ["apple", "racecar", "helmet", "green", "juice", "money"]
# random_word = words[random.randint(0, len(words) - 1)]

def display_hangman(chance: int) -> str:
    """
    Displays hangman ascii art

    For more ascii arts like this, visit https://ascii.co.uk/
    """

    ascii_hangman = [r"""
                        _______
                        |/      |
                        |      (_)
                        |      /|\
                        |       |
                        |      / \
                        |
                     ___|___""",
                     r"""
                        _______
                        |/      |
                        |      (_)
                        |      /|\
                        |       |
                        |        \
                        |
                     ___|___""",
                     r"""
                        _______
                        |/      |
                        |      (_)
                        |      /|\
                        |       |
                        |      
                        |
                     ___|___""",
                     r"""
                        _______
                        |/      |
                        |      (_)
                        |      /|
                        |       |
                        |        
                        |
                     ___|___""",
                     r"""
                        _______
                        |/      |
                        |      (_)
                        |       |
                        |       |
                        |        
                        |
                     ___|___"""]

    for index, val in enumerate(ascii_hangman, start=1):
        if chance == index:
            print(val)

def reset():
    """
    Resets the game
    """

    play_again = input("Do you want to play again? [y/n]: ").lower()
    if play_again == "y":
        return main()
    elif play_again == "n":
        quit()
    else:
        print("Invalid choice. Exiting...")
        quit()

def play():
    """
    ==================================================================================================
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/                       
    
    Mechanics of the game:
    
    - The hangman consist of a head, a body, 2 arms, and 2 legs.
    - If the guessing player correctly guesses the puzzle or fills in all 
        of the letters before the hangman is complete, they win and the hangman lives.
    - Or the hangman will be executed

    Good luck!
    ==================================================================================================
    """

    global chances
    random_word = random.choice(words)
    word_placeholder = ["_" for c in random_word]
    while True:
        print(" ".join(word_placeholder))
        print()
        if "_" in word_placeholder:
            guess = str(input("Guess a letter: ")).lower()
            print()
            if chances >= 1:
                if not guess:  
                    print("You must enter a guess.")
                elif guess.isdigit():
                    print("Invalid numeric ")
                elif guess in random_word:
                    for index in range(len(random_word)):
                        if guess == random_word[index]:
                            word_placeholder[index] = guess
                    continue
                else:
                    display_hangman(chances)
                    print("Remaining chances: {}".format(str(chances)))
                    chances -= 1
            else:   
                print("You run out of chances. Game over.\n")
                chances = 4
                reset() # Resets the game
        else:
            print("You did it! You've guessed the word {}.".format(random_word))
            chances = 4
            reset() # Resets the game

def main():
    os.system('cls') # Clears terminal 
    print(play.__doc__) # Prints the welcome message and mechanics of the game
    display_hangman(5) # Displays ascii hangman
    play() # Start playing

if __name__ == "__main__":
    main()