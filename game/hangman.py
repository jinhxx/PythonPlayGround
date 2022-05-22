import random
import string


def hangman():
    cnt = 6
    words = ["apple", "orange", "banana", "melon"]
    word = random.choice(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting user input
    while len(word_letters) > 0 and cnt > 0:
        print('-'*40, '\nYou have used these letters : ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(f"Current word : {' '.join(word_list)}")

        user_letter = input('Guess a latter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                cnt -= 1
                print('>>>>> Letter is not in word!')
        elif user_letter in used_letters:
            print('>>>>> You have a already used that character. try again!')
        else:
            print('>>>>> Invalid characters try again!')

    if cnt == 0:
        print('#### Game over!! T_T ####')
    else:
        print(f'----- You guessed the word! -> answer : {word}!! -----')


hangman()
