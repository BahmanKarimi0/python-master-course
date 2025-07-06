"""
Exercise 04‑01 – basic if/elif/else with temperature units
"""
try:
    temperature_str = input("Enter temperature (e.g. 30): ").strip()
    units_str = input("Enter units (e.g. 'C' for Centigrade of 'F' for Fahrenheit ): ").strip().casefold()
    if not temperature_str or not units_str:
        print("⚠️  Temperature and Unit cannot be empty.")
        exit()
    if units_str not in ['c', 'f']:
        print("⚠️  Unknown units.")
        exit()
    temperature = float(temperature_str)
    if units_str == "c" and temperature > 30:
        print('Hot in celsius')
    elif units_str == "f" and temperature > 86:
        print('Hot in fahrenheit')
    else:
        print('Moderate')

except ValueError:
    print("⚠️  Invalid input.")