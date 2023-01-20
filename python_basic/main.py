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
# a: الگوریتم محاسبه ب.م.م : بزرگترین مقسوم علیه ( شمارنده ) مشترک 
# (num1 , num2 ) 
num1:int = int( input("Enter number 1 of (num1 , num2): ") )
num2:int = int( input("Enter number 2 of (num1 , num2): ") )

max_num = max(num1 , num2)  # iter in (num1 , num2 )
min_num = min(num1 , num2)
bmm = 0
if max_num % min_num == 0 :
     bmm = min_num
else:
     m = max_num % min_num
     
	# this is just for test 
if result == None:
	print("The Numbr <1>")
else:
	print( f"The Number is <{result}>")

