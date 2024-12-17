def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("====================")
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
    temp = float(input("Enter the temperature value: "))

    if unit == "C":
        print(temp, "°C is equal to:")
        print(round(celsius_to_fahrenheit(temp), 2), "°F")
        print(round(celsius_to_kelvin(temp), 2), "K")
    elif unit == "F":
        print(temp, "°F is equal to:")
        print(round(fahrenheit_to_celsius(temp), 2), "°C")
        print(round(fahrenheit_to_kelvin(temp), 2), "K")
    elif unit == "K":
        print(temp, "K is equal to:")
        print(round(kelvin_to_celsius(temp), 2), "°C")
        print(round(kelvin_to_fahrenheit(temp), 2), "°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
