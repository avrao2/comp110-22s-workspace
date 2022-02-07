"""EX03 - Structured Wordle."""

__author__ = "730478127"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(string1: str, string_one_character: str) -> bool: 
    """Checks if the character of the second string is found in the first string."""
    assert len(string_one_character) == 1
    i: int = 0
    while i < len(string1):
        if string_one_character == string1[i]:   # checks if the character of the second string is found at any index of the first string 
            return True
        else: 
            i += 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """Assigns emojis based on if each character of guess is not contained in the word, contained but at the wrong index, or at the correct index of the secret word."""
    assert len(guess) == len(secret)
    index: int = 0
    emoji: str = ""
    while index < len(guess):
        if guess[index] == secret[index]:   # if the letter is in the secret word and at the right index
            emoji += GREEN_BOX  
        elif contains_char(secret, guess[index]) is True:   # if the letter is in the secret word but at the wrong index
            emoji += YELLOW_BOX  
        else:   # if the letter is not in the secret word
            emoji += WHITE_BOX   
        index += 1 
    return emoji 


def input_guess(guess_expected_length: int) -> str:
    """Makes sure the user's guess is the same length as the secret word."""
    user_guess: str = input(f"Enter a { guess_expected_length } character word: ")   # prompts user to make a guess
    while len(user_guess) != guess_expected_length: 
        user_guess = input(f"That wasn't { guess_expected_length } chars! Try again: ")   # ensures the guess is the correct length
    return user_guess 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    win: bool = False
    while turns < 6 and win is not True:   # if the user still has turns left and has not guessed the word yet, then the loop will continue to run
        print(f"=== Turn {turns}/6 ===")
        user_guess: str = input_guess(5)
        print(emojified(user_guess, "codes"))
        if user_guess == secret_word:
            win = True
        else: 
            turns += 1
    if win is True:   # the user has won the game
        print(f"You won in {turns}/6 turns!")
    else:   # the user has used up all of their turns but has not guessed the secret word
        print("X/6 - Sorry, try again tomorrow!") 
    

if __name__ == "__main__":
    main()













