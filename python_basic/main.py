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




def roll(roll_number,dic_side_number):
    def roll_dice():
        import random
        random.seed()
        # random.seed(23*99-6%60) get random 4 -.-
        return random.randint(1, dic_side_number)
    dice_dic ={}
    for side in range(dic_side_number):
        dice_dic[side+1] = 0
    # creating the dataset
    # is there any one line for to fill it ?
    for i in range(roll_number): dice_dic[roll_dice()] += 1
    return dice_dic

def plot_data(dic,y_label,x_lable):
    import matplotlib.pyplot as plt
    plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    objects = dic.keys()
    performance = dic.values()
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel(y_label)
    plt.title(x_lable)
    plt.show()


def dice_plot(roll_number,dice_side):
    data = roll(roll_number,dice_side)
    plot_data(data,y_label='rolls',x_lable='dice_number')

dice_plot(549,9)