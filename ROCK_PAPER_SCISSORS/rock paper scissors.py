import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand=[rock,paper,scissors]
user_choice=int(input("what you choose!! Type 0 for rock, 1 for Paper,2 for scissors: "))
if user_choice>=3 or user_choice<0:
    print("Invalid Number!! You Loose")
else:
    print(hand[user_choice])

computer_choice=random.randint(0,2)

print(f"Computer choose: ")
print(hand[computer_choice])


if user_choice>=3 or user_choice<0:
    print("Invalid Number!! You Loose")

elif user_choice == 0 and computer_choice==2:
    print("You win")
elif computer_choice == 0 and user_choice==2:
    print("You Loose!! Computer Wins")
elif computer_choice>user_choice:
    print("You Loose!! Computer wins")
elif user_choice>computer_choice:
    print("You win")
elif user_choice == computer_choice:
    print("Draw!")

    