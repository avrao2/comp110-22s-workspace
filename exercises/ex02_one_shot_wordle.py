"""EX02 - One-Shot Wordle."""

__author__ = "730478127"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python"
guess: str = input(f"What is your { len(secret_word) }-letter guess? ")
index: int = 0
emoji: str = ""
while len(guess) > len(secret_word) or len(guess) < len(secret_word):
    guess = input(f"That was not { len(secret_word) } letters! Try again: ")
while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji += GREEN_BOX   # if letter is in the right place
    else: 
        character_exists: bool = False
        check_index: int = 0
        while character_exists is not True and check_index < len(secret_word): 
            if guess[index] == secret_word[check_index]:
                character_exists = True 
            else:
                check_index += 1 
        if character_exists is True: 
            emoji += YELLOW_BOX   # if letter is in the word but at a different index
        else:
            emoji += WHITE_BOX   # if letter is not in the word
    index = index + 1 
print(emoji) 


if len(guess) == len(secret_word):
    if guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!") 
