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
from random import randint
dice = [0,0,0,0,0,0]
for i in range(10000):
    dice_roll  = randint(1,6)
    if dice_roll == 1 :
        dice[0] +=1
    elif dice_roll == 2 :
        dice[1] +=1
    elif dice_roll == 3 :
        dice[2] +=1
    elif dice_roll == 4 :
        dice[3] +=1
    elif dice_roll == 5 :
        dice[4] +=1
    elif dice_roll == 6 :
        dice[5] +=1

print(dice)