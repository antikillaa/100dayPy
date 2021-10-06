import random
import replit
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 6
stages = hangman_art.stages
while not end_of_game:
    guess = input("Choose a letter: ").lower()
    replit.clear()

    if guess in display:
        print(f"You've already guessed: {guess}")

    for i in range(len(display)):
        if chosen_word[i] == guess:
            display[i] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The guessed word was: {chosen_word}")

    if not "_" in display:
        end_of_game = True
        print("You win!")


    print(stages[lives])
