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

#Simple two numbers BMM calculator using python -------------------------------------------------------------------------------------

def find_bmm():
    first_number = int(input('enter first number :'))
    second_number = int(input('enter second number :'))
    min_num = min(first_number,second_number)
    max_num = max(first_number,second_number)
    bmm = 0
    for i in range(max_num):
        if max_num%min_num == 0 :
            bmm = min_num
            break 
        elif max_num%min_num != 0:
            bmm = max_num%min_num
            max_num = min_num
            min_num = bmm
            if bmm % min_num == 0 :
                break
    print(f'BMM of [{first_number}]-[{second_number}] : is {bmm}')

            
find_bmm()