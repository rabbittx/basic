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

#-------------------------------------------------------------------------------------



