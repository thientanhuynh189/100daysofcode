# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)
bmi_round1 = round(bmi,1)
bmi_round = round(bmi)
if bmi_round1 < 18.5:
  result = "underweight"
elif bmi_round1 < 25:
  result = "normal weight"
elif bmi_round1 < 30:
  result = "overweight"
elif bmi_round1 < 35:
  result = "obese"
else:
  result = "clinically obese"
print(f"Your BMI is {bmi_round}, you are {result}")