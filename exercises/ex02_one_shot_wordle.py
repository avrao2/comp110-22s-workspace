"""EX02 - One-Shot Wordle."""

__author__ = "730478127"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
index: int = 0
emoji: str = ""
while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji += GREEN_BOX
    else: 
        character_exists: bool = False
        check_index: int = 0
        while character_exists is not True and check_index < len(secret_word): 
            if guess[index] == secret_word[check_index]:
                character_exists = True 
            else:
                check_index += 1 
        if character_exists is True: 
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    index = index + 1 
print(emoji)


if len(guess) == len(secret_word):
    if guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!") 
