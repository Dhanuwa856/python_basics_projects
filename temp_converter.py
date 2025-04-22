# Temperature Converter CLI

def fahrenheit_to_celsius(x):
    c = round((x - 32) / (9 / 5), 2)
    return f"{c} °C"

def celsius_to_fahrenheit(x):
    f = round((x * (9/5) + 32), 2)
    return f"{f} °F"


def temperature_converter():
    while True:
        print("1. Fahrenheit °F to Celsius °C")
        print("2. Celsius °C to Fahrenheit °F")
        print("3. Exit")

        try:
            userinput = float(input("Enter temperature value: "))

            choice = int(input("Select Option: "))
            if choice == 1:
                print(fahrenheit_to_celsius(userinput))
            elif choice == 2:
                print(celsius_to_fahrenheit(userinput))
            elif choice == 3:
                break
            else:
                print("Enter 1-3 Number")
        except ValueError:
            print("Enter Number !")

temperature_converter()