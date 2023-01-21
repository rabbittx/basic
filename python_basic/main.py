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
    dice = random.randint(1,6)
    return dice

dice_list = [0,0,0,0,0,0]
for i in range(10000):
    dice  = roll_dice()
    # print(dice)
    if dice == 1 :
        dice_list[0] +=1
    elif dice == 2 :
        dice_list[1] +=1
    elif dice == 3 :
        dice_list[2] +=1
    elif dice == 4 :
        dice_list[3] +=1
    elif dice == 5 :
        dice_list[4] +=1
    elif dice == 6 :
        dice_list[5] +=1

import numpy as np
import pandas as pd
from matplotlib.pyplot import plot
# output_notebook() # uncomment this for use in a notebook

SIZES = (10, 50, 100, 500, 1000, 5000, 10000, 50000)
BINS = np.arange(14) - 0.5
random.seed(5864218/8*236)
def roll():
    return random.randint(1,6)

roll_dice_number = 0
import numpy as np
import matplotlib.pyplot as plt
dice_dic = {1:0,2:0,3:0,4:0,5:0,6:0}
# creating the dataset
for i in range(10000):
    data = roll()
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
import numpy as np

import matplotlib.pyplot as plt


plt.show()