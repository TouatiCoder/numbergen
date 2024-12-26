from pyfiglet import figlet_format
import random
from datetime import datetime

# Generate the logo using pyfiglet
def print_touati_logo():
    logo = figlet_format('TOUATI', font='slant')  # You can change 'slant' to any font you prefer
    print(logo)
    print("Auth:")
    print("Fb: https://web.facebook.com/touati.ayoub02/")

# Display the logo
print_touati_logo()

# List of countries with their phone codes, number prefixes, and number lengths
countries = {
    1: {'name': 'Morocco', 'code': '212', 'prefixes': ['6', '7'], 'length': 9},
    2: {'name': 'Algeria', 'code': '213', 'prefixes': ['5', '6', '7'], 'length': 9},
    3: {'name': 'Tunisia', 'code': '216', 'prefixes': ['2', '5', '9'], 'length': 8},
    4: {'name': 'Egypt', 'code': '20', 'prefixes': ['10', '11', '12', '15'], 'length': 10},
    5: {'name': 'USA', 'code': '1', 'prefixes': [''], 'length': 10},
    6: {'name': 'Canada', 'code': '1', 'prefixes': [''], 'length': 10},
    7: {'name': 'France', 'code': '33', 'prefixes': ['6', '7'], 'length': 9},
    8: {'name': 'Germany', 'code': '49', 'prefixes': ['15', '16', '17'], 'length': 10},
    9: {'name': 'UK', 'code': '44', 'prefixes': ['7'], 'length': 10},
    10: {'name': 'Spain', 'code': '34', 'prefixes': ['6', '7'], 'length': 9},
    11: {'name': 'Italy', 'code': '39', 'prefixes': ['3'], 'length': 10},
    12: {'name': 'Saudi Arabia', 'code': '966', 'prefixes': ['5'], 'length': 9},
    13: {'name': 'UAE', 'code': '971', 'prefixes': ['50', '55', '56'], 'length': 9},
    14: {'name': 'Qatar', 'code': '974', 'prefixes': ['3', '5', '6', '7'], 'length': 8},
    15: {'name': 'Australia', 'code': '61', 'prefixes': ['4'], 'length': 9},
    16: {'name': 'Japan', 'code': '81', 'prefixes': ['70', '80', '90'], 'length': 10},
    17: {'name': 'China', 'code': '86', 'prefixes': ['13', '15', '18'], 'length': 11},
    18: {'name': 'India', 'code': '91', 'prefixes': ['7', '8', '9'], 'length': 10},
    19: {'name': 'Brazil', 'code': '55', 'prefixes': ['9'], 'length': 11},
    20: {'name': 'Mexico', 'code': '52', 'prefixes': ['1'], 'length': 10},
    21: {'name': 'South Africa', 'code': '27', 'prefixes': ['6', '7'], 'length': 9},
    22: {'name': 'Nigeria', 'code': '234', 'prefixes': ['70', '80', '81'], 'length': 10},
    23: {'name': 'Kenya', 'code': '254', 'prefixes': ['7'], 'length': 9},
    24: {'name': 'Russia', 'code': '7', 'prefixes': ['9'], 'length': 10},
    25: {'name': 'Turkey', 'code': '90', 'prefixes': ['5'], 'length': 10},
}

# Generate valid phone numbers based on the selected country with validation
def generate_valid_phone_numbers(count, country_code):
    country = countries.get(country_code)
    
    if not country:
        print("Sorry, the code {} is not in the list.".format(country_code))
        return
    
    country_dial_code = country['code']
    phone_length = country['length']
    prefixes = country['prefixes']
    
    # Use the current date and time as part of the file name
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "valid_numbers_{}.txt".format(current_time)
    
    with open(file_name, 'w') as f:
        for i in range(count):
            # Choose a valid prefix randomly
            prefix = random.choice(prefixes)
            # Generate the remaining part of the phone number
            number_length = phone_length - len(prefix)  # Subtract prefix length from total phone number length
            number = ''.join([str(random.randint(0, 9)) for _ in range(number_length)])
            full_number = "+{}{}{}".format(country_dial_code, prefix, number)  # Include country code
            f.write("{}\n".format(full_number))
            print(full_number)
    
    print("Valid numbers generated and saved in file {}".format(file_name))

# Display the list of countries for selection
def show_country_options():
    print("Choose a country to generate phone numbers:")
    for code, country in countries.items():
        print("{}- {}".format(code, country['name']))

# Execute the program
show_country_options()
selected_country_code = int(input("Enter the country number for which you want to generate numbers: "))
number_count = int(input("Enter the number of phone numbers you want to generate: "))

generate_valid_phone_numbers(number_count, selected_country_code)
