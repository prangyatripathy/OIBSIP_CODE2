def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def user_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers we cant give negatives.")
        
        return weight, height
    except ValueError as e:
        print(f"Invalid input: {e}")
        return user_input()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    weight, height = user_input()
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print(f"Your BMI is {bmi:.2f}, which is considered {category}.")

if __name__ == "__main__":
    main()
