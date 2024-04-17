import os
import function as f
from datetime import datetime
import time
import money as m

import mysql.connector

def dep_with():
    f.login()
    bal = 1200.00

    print(f'Here is your current balance: {bal}')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    os.system('cls')
    wd = input('Do you want to deposit or withdraw from your balance? (w/d): ')
    if wd == 'w':
        w = float(input('How much money do you want to withdraw?: '))
        if total >= w:
            total = bal - w
            print(f'Your new balance is {total}')
            time.sleep(2)
            options()

    if wd == 'd':
        d = float(input('How much money do you want to deposit?: '))
        total = bal + d
        print(f'Your new balance is {total}')
        time.sleep(3)
        options()


dep_with()