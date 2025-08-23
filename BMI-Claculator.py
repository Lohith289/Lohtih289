def BMI_calcutor():
    x = input("Enter you name : ")
    print(f"\n === Hi {x} Let's calculate your BMI Today !!!!! ===")
    a = float(input("Enter your weight in Kilograms : "))
    b = float(input("Enter your height in Meters : "))
    c = int(a / (b**2))
    print(c)

print(BMI_calcutor())