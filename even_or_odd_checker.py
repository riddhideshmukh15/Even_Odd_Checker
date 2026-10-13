

while True:
    num = int(input("Enter your number: "))

    if num == 0:
        print("Number is zero")
    elif num > 0:
        print("Number is positive")
    else:
        print("Number is negative")

    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

    choice = input(
        "\nDo you want to check another number? (yes/no): "
    )

    if choice.lower() != "yes":
        print("Thank you for using Number Checker!")
        break
