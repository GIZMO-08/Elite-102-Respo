import os
import function as f
from datetime import datetime
import time

def x(choice):

    
    if choice == 1:
        os.system('cls')
        print("Please enter in your age: ")
        age = int(input())
    if age >= 18:
        f.signup()
        f.per_info()
        f.secure()
        f.ok()
        credit = True
        options()



    elif age <= 17:
      f.joint()
      f.per_info()
      f.secure()
      f.ok()
      credit = True
      options()
    elif choice == 2:
        print("Please enter in your age: ")
        age = int(input())
        if age >= 18:
            f.signup()
            f.per_info()
            f.secure()
            f.ok()
            saving = True
            options()

        elif age <= 17:
            f.joint()
            f.per_info()
            f.secure()
            f.ok()
            saving = True
            options()
    elif choice == 3:
        print("Please enter in your age: ")
        age = int(input())
        if age >= 18:
            f.signup()
            f.per_info()
            f.secure()
            f.ok()
            bank = True
            options()

        elif age <= 17:
            f.joint()
            f.per_info()
            f.secure()
            f.ok()
            bank = True
            options()
    elif choice == 4:
        print("Bot: Ok! Thank you for using the Banker ChatBot!")


    if credit == True:
        if choice == 1:
            print(f"You already signed up to this account.")
            print("You can choose to create another account,or exit out of the program")
            options()


    """
    if saving == True:
    if choice == 2:
        print(f"You already signed up to this account  {name}")
        print("You can choose to create another account,or exit out of the program")
        options(name)
    """


