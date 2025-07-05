"""
mini_project_bmi_calculator.py
A small program to calculate and classify Body Mass Index (BMI)
"""

try:
    height_str = input("Enter your height in m (e.g. 1.93): ").strip()
    weight_str = input("Enter your weight in kg (e.g. 90): ").strip()
    if not height_str or not weight_str:
        print("⚠️  Height and weight cannot be empty.")
        exit()
    height = float(height_str)
    weight = float(weight_str)
    if height <= 0 or weight <= 0:
        print("⚠️  Height and weight must be positive numbers.")
        exit()
    bmi = round(weight / height ** 2, 2)
    print(f'Your BMI is {bmi} kg/m²')

    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 25:
        category = 'Normal weight'
    elif 25 <= bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obesity'
    print(f"Category: {category}")
except ValueError:
    print("⚠️  Invalid input. Please enter numeric values only.")

