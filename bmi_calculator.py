weight = 85  # weight in kilograms
height = 1.85  # height in meters

# Calculate BMI
bmi = weight / (height ** 2)

# Interpret the BMI
if bmi < 18.5:
    print(f"BMI: {bmi:.2f} - underweight")
elif 18.5 <= bmi < 25:
    print(f"BMI: {bmi:.2f} - normal weight")
else:
    print(f"BMI: {bmi:.2f} - overweight")
