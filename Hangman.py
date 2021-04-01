import functions
import turtle


def main():
    print_header()
    functions.draw_pole()
    print("Let's play Hangman")
    print("Guess the letters in the word I'm thinking of...")
    print()
    play_word = functions.word_generator()
    play_letters = functions.letters_of_word(play_word)
    run_event_loop(play_letters, play_word)


def print_header():
    print("---------------------------------------")
    print("               HANGMAN                 ")
    print("---------------------------------------")
    print()


def run_event_loop(letters, word):
    t = turtle.Turtle()
    turns = 6
    failed = 0
    guesses = []

    while turns > 0 and failed < 6:
        guess = input("Letter: ")
        guess = guess.lower().strip()

        if not guess or not guess.strip():
            print("Words are made up of letters")
        elif guess in letters:
            if guess in guesses:
                print("Oops. Looks like you already guessed that.")
            else:
                print([guess if guess == letter else '_' for letter in letters])
        else:
            failed += 1
            turns -= 1
            print(f"Nope, you have {turns} turns left")
            functions.steps_hangman(t, turns+1)
        guesses.append(guess)

    print(f"Sorry. The word was {word.upper()}. You loose")


if __name__ == '__main__':
    main()
