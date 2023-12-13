# import os
# if __name__=='__main__':
#     print("Welcome to robo speaker")
#     x=input("Enter what you want to speak: ")
#     command=f"say {x}"
#     os.system(command)

import pyttsx3

if __name__=='__main__':
    print("Welcome to robo speaker")
    while True:
        x = input("Enter what you want to speak: ")
        if x=="q":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
