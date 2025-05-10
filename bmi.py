weight = float(input("Enter your weight in kg: ")) 
height = float(input("Enter your height in cm: "))  
bmi = (weight / (height * height)) * 10000  
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight,Eat more.")
elif 18.5 <= bmi < 24.9:
    print("You are normal weight,Keep it up!")
elif 25 <= bmi < 29.9:
    print("You are overweight,Conider hitting the gym.")
elif 30 <= bmi < 34.9:
    print("You have obesity class 1.")
elif 35 <= bmi < 39.9:
    print("You have obesity class 2.")
else:
    print("You have obesity class 3.")

# This code calculates the Body Mass Index (BMI) based on user input for weight and height.