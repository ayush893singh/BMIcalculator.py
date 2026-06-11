print("===== BMI Calculator =====")

weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print(f"\nYour BMI is: {round(bmi, 2)}")

if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal Weight")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese") 