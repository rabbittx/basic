#Simple BMI calculator using python -------------------------------------------------
def bodymassindex(height, weight):
    return weight / (height/100)**2

def calculator_BMI():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    bmi = bodymassindex(height, weight)
    print(F"Your BMI is: {bmi}")
    if bmi <= 18.5:
        print("You are underweight.")
    elif 18.5 < bmi <= 24.9:
        print("Your weight is normal.")
    elif 25 < bmi <= 29.29:
        print("You are overweight.")
    else:
        print("You are obese.")

# calculator_BMI()


#Simple two number BMM calculator using python -------------------------------------------------------------------------------------

def find_bmm():
    # find bmm of 2 number
    first_number = int(input('enter first number :'))
    second_number = int(input('enter second number :'))
    min_num = min(first_number,second_number)
    max_num = max(first_number,second_number)

    for i in range(min_num):
        bmm = min_num if max_num % min_num == 0 else max_num % min_num
        max_num , min_num = min_num , bmm 
        if bmm % min_num == 0 :
            break

        # if max_num%min_num == 0 :
        #     bmm = min_num
        #     break 
        # elif max_num%min_num != 0:
        #     bmm = max_num%min_num
        #     max_num = min_num
        #     min_num = bmm
        #     if bmm % min_num == 0 :
        #         break

    print(f'BMM of [{first_number}]-[{second_number}] : is {bmm}')


#Simple Graph Plotting in Python -------------------------------------------------------------------------------------

import random 

def roll_dice():
    # random.seed(23*99-6%60) get random 4 -.-
    return random.randint(1,6)


import numpy as np
import pandas as pd
from matplotlib.pyplot import plot

dice_dic = {1:0,2:0,3:0,4:0,5:0,6:0}
# creating the dataset
for i in range(10000):
    data = roll_dice()
    if data == 1 :
        dice_dic[1] +=1
    elif data == 2 :
        dice_dic[2] +=1
    elif data == 3 :
        dice_dic[3] +=1
    elif data == 4 :
        dice_dic[4] +=1
    elif data == 5 :
        dice_dic[5] +=1
    elif data == 6 :
        dice_dic[6] +=1


print(dice_dic)



plot.show()