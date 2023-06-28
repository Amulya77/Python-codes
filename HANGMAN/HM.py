import random

word_list = ["advark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# ln_cw = len(chosen_word)


# #lst = [None] * ln_cw
# lst = ["_"] * ln_cw  # Create a list of underscores
# #lst=["_" for i in range(int(input()))]
# lst_string = ''.join(lst)
# print(lst_string)

# xs = ['1', '2', '3']
# s = ''.join(xs)
# print(s)


display=[]
#for letter in chosen_word:
for _ in range(len(chosen_word)):
    display+="_"
print(display)




#1 intendation= 4 blanks!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#(CTRL+])     to shift to 1 indentation in python

end_of_game=False 

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #for letter in chosen_word:
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
        #     print("Right")
        # else:
        #     print("Wrong")
            display[position]=letter

    print(display)  

    if "_" not in display:
        end_of_game=True
        print("You WIN!!!")