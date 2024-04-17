import os
import function as f
from datetime import datetime
import time



import mysql.connector


def signup():
  print("Welcome to the sign up page!")
  print(" ")
  print("Please enter your email:")
  email = input()
  print("Please enter your first name:")
  first = input()
  print("Please enter your last name:")
  last = input()
  print(" ")
  print("Please enter your phone number:")
  phone = input()
  print(" ")
  print("Please enter your age:")
  age = int(input())
  print(" ")
  print("Please enter your username:")
  username = input()
  print(" ")
  print("Please enter your password:")
  password = input()
  print(" ")
  os.system('cls')
  print("Type in your password again to confirm:")
  two = input()
  if password == two:
    os.system('cls')
    print(f"Ok! Your username is {username} and your password is {password}")
    connection = mysql.connector.connect(user='root', database='users', password='GIZ!MONEA2020!')
    cursor = connection.cursor()
    sql = "INSERT INTO user_tbl (FirstName, LastName, UserName, Pasword, Age, PhoneNum) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (first,last, username, password, age, phone)
    cursor.execute(sql, val)
    conn.commit()

    time.sleep(2)
    os.system('cls')
    cursor.close()
    connection.close()


  else:
    print("Passwords do not match. Please try again.")
    signup()
  

def per_info():
  print("Please answer the questions below to finish your profile.")
  print("Please enter your gender:")
  gender = input()
  os.system('cls')


def secure():
  print("Here is some security questions to help you secure your account.")
  print("Please enter your city:")
  city = input()
  print("Please enter your state:")
  state = input()
  print("What is the name of your pet?:")
  pet = input()
  print("What is the name of your favorite food?:")
  food = input()
  print("What school did you attend:")
  school = input()
  os.system('cls')
  print("Ok! Lets see your results!")
  print(f"You're living in {city},{state}")
  print(f"Your pet's name is {pet}")
  print(f"your favorite food is {food}")
  print(f"You went to school at {school}")


def joint():
  print("Welcome to the joint page!")
  print("Do your parents have an account on the banking site?: (y/n) ")
  print(" ")
  answer = input()
  if answer == 'y':
    print("Please create your username")
    username2 = input()
    print(" ")
    print("Please create your password")
    password2 = input()
    print(" ")
    print("Please enter your email:")
    email = input()
    print(" ")
    print("Please enter your parent's phone number:")
    phone = input()
    print(" ")
    print("Please enter your username:")
    username3 = input()
    print(" ")
    print("Please enter your password:")
    password3 = input()
    print(" ")
    print("Type in your password again to confirm:ssword again to confirm:")
    two = input()
    if password3 == two:
      for i in password2:
        password2 = print("*")

      print(f"Ok! Your username is {username2} and your password is {password2}")
  else:
    print("Please create your parent's username")
    username2 = input()
    print(" ")
    print("Please create your parent's password")
    password2 = input()
    print(" ")
    print("Please enter their email:")
    email = input()
    print(" ")
    print("Please enter their phone number:")
    phone = input()
    print(" ")
    print("Please enter their username:")
    username3 = input()
    print(" ")
    print("Please enter their password:")
    password3 = input()
    print(" ")
    print("Type in their password again to confirm:")
    two = input()
    print(" ")
    if password3 == two:
      print(f"Ok! Your username is {username2} and your password is {password2}")
      print(" ")
    print("Did you finish their profile?: (y/n)")
    profile = input()
    if profile == 'y':
      print("Ok. Its time to start working on yours!")
      os.system('clear')
      print("Please create your username")
      username2 = input()
      print("")
      print("Please create your password")
      password2 = input()
      print("")
      print("Please enter your email:")
      email = input()
      print("")
      print("Please enter your parent's phone number:")
      phone = input()
      print("")
      print("Please enter your username:")
      username3 = input()
      print("")
      print("Please enter your password:")
      password3 = input()
      print("")
      print("Type in your password again to confirm:ssword again to confirm:")
      two = input()
      if password3 == two:
        print("")
        print(f"Ok! Your username is {username2} and your password is {password2}")

def ok():

  print("Do you want to confirm your profile?: (y/n)")
  confirm = input()
  if confirm == 'y':
    print("Ok! Thank you for creating this account!")
    os.system('clear')


def login():

  connection = mysql.connector.connect(user='root', database='users', password='GIZ!MONEA2020!')
  cursor = connection.cursor()

  user = input("Please enter your username: ")
  pwd = input("Please enter your password: ")

  query = "SELECT UserName, Pasword FROM user_tbl WHERE UserName = %s"
  cursor.execute(query, (user,))
  user_record = cursor.fetchone()


  if user_record:
    stored_password = user_record[1] 
    if pwd == stored_password:
      print(f"Welcome back, {user}!")
    else:
      print("Invalid password. Please try again.")
  else:
      print("Invalid username. Please try again.")

  cursor.close()
  connection.close()

signup()