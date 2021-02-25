age = input("What is your current age")

day_90 = 365 * 90
week_90 = 52 * 90
month_90 = 12 * 90

day = day_90 - (int(age) * 365)
week = week_90 - (int(age) * 52)
month = month_90 - (int(age) * 12)

print(f"You have {day} days, {week} weeks and {month} months left.")