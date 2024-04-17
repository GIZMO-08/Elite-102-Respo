import os
import function as f
from datetime import datetime
import time
import money as m



import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'users', password = 'GIZ!MONEA2020!')

host = "127.0.0.1"
username = "root"
password = "GIZ!MONEA2020!"
database = "users"


def startup():
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(2)
  os.system('cls')
  print("Please type 'Hi' when you're ready to begin")
  
  hi = input("You: ")
  if hi == 'Hi' or hi == 'hi' or hi == 'HI':
     os.system('cls')
     print('Bot: Hello! Welcome to the official Peoples Banker ChatBot!')
     print('Can you type in your name?')
     name = input('You: ')
     print('Bot: Hello ' + name + '!')
     print('Bot: Are you ready to start?: (y/n)')
     ready = input('You: ')
     if ready == 'y':
         print('Bot: Great! Lets get started!')
         time.sleep(1)
         os.system('cls')
         print('Bot: Here are your options:')
         options()
     elif ready == 'n':
       print("Ok! Goodbye!")
       exit()
     else:
       print("Bot:SyStEM ShUttIng DoWN")
       time.sleep(2)
       os.system('cls')
       exit()
  else:
    print("Invalid entry")
    print("Premature exit")
    exit()
     

def options():
  print('1. Credit Card Account')
  print('2. Savings Account')
  print('3. Bank Account')
  print('4. Withdraw/Deposit')
  print('4. Exit')
  print("Bot: Type in which option you want to select.")
  choice = int(input("You: "))
  
  if choice == 1:
    os.system('cls')
    yes = input("Did you already create an account?(y/n): ")
    if yes == 'y':
      f.login()
    if yes == 'n':
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
  if choice == 2:
      os.system('cls')
      yes = input("Did you already create an account?(y/n): ")
      if yes == 'y':
        f.login()
      if yes == 'n':
        print("Please enter in your age: ")
        age = int(input())
        if age >= 18:
          f.signup()
          os.system('cls')
          f.per_info()
          os.system('cls')
          f.secure()
          os.system('cls')
          f.ok()
          saving = True
          os.system('cls')
          options()
    
        elif age <= 17:
          f.joint()
          os.system('cls')
          f.per_info()
          os.system('cls')
          f.secure()
          os.system('cls')
          f.ok()
          saving = True
          os.system('cls')
          options()
  if choice == 3:
    os.system('cls')
    yes = input("Did you already create an account?(y/n): ")
    if yes == 'y':
      f.login()
    if yes == 'n':
      print("Please enter in your age: ")
      age = int(input())
      if age >= 18:
        f.signup()
        os.system('cls')
        f.per_info()
        os.system('cls')
        f.secure()
        os.system('cls')
        f.ok()
        bank = True
        os.system('cls')
        options()
    
      elif age <= 17:
        f.joint()
        os.system('cls')
        f.per_info()
        os.system('cls')
        f.secure()
        os.system('cls')
        f.ok()
        bank = True
        os.system('cls')
        options()
  if choice == 4:
    m.dep_with()
    options()
  elif choice == 5:
    print("Thank you for using the official Peoples ChatBot!")
    print("Bye!!!")
    time.sleep(3)
    os.system('cls')


#startup()

#options()