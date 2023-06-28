import random
# had to turn some of these to raw ("r") strings, so "\" are not treated as escape characters
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["advark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_ln=len(chosen_word)

lives=6


display=[]

for _ in range(len(chosen_word)):
    display+="_"
print(display)


end_of_game=False 

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter
    
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You LOSE!!!!!")

    print(display)  

    if "_" not in display:
        end_of_game=True
        print("You WIN!!!")


    print(stages[lives])    