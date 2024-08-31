weight = int(input("enter weight: "))
height = int(input("height in cms : "))

bmi = weight / (height/100) ** 2


print(f"your BMI for height {height} and weight {weight} is {bmi}")