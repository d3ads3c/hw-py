si = input("Do You Like Use 'SI' : ")
if si == "yes":
    weight = float(input("Enter your weight (lb) :"))
    height = float(input("Enter your height (in) : "))
    bmi = (weight /(height ** 2)) * 703
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 < bmi < 25:
        print("Normal")
    elif 25 < bmi < 30:
        print("Overweight")
    else:
        print("Obesity")
elif si == "no":
    weight = float(input("Enter your weight (KG) :"))
    height = float(input("Enter your height (M) : "))
    bmi = (weight ** 2) / height
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 < bmi < 25:
        print("Normal")
    elif 25 < bmi < 30:
        print("Overweight")
    else:
        print("Obesity")
