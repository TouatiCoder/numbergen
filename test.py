from pyrogram import Client
from pyfiglet import figlet_format
import random
from datetime import datetime

# إعدادات Telegram API
api_id = 1864213005  # استبدل بـ API ID الخاص بك
api_hash = "20cf9649621e5c5b140760fa9b1d0feb"  # استبدل بـ API Hash الخاص بك

# إنشاء تطبيق Telegram
app = Client("telegram_checker", api_id=api_id, api_hash=api_hash)

# قائمة الدول مع الأكواد والمعلومات الخاصة بها
countries = {
    1: {'name': 'Morocco', 'code': '212', 'prefixes': ['6', '7'], 'length': 9},
    2: {'name': 'Algeria', 'code': '213', 'prefixes': ['5', '6', '7'], 'length': 9},
    3: {'name': 'Tunisia', 'code': '216', 'prefixes': ['2', '5', '9'], 'length': 8},
    4: {'name': 'Egypt', 'code': '20', 'prefixes': ['10', '11', '12', '15'], 'length': 10},
    5: {'name': 'Saudi Arabia', 'code': '966', 'prefixes': ['5'], 'length': 9},
}

# عرض الشعار
def print_touati_logo():
    logo = figlet_format('TOUATI', font='slant')
    print(logo)
    print("Auth:")
    print("Fb: https://web.facebook.com/touati.ayoub02/")

# عرض قائمة الدول للاختيار
def show_country_options():
    print("Choose a country to generate and filter numbers:")
    for code, country in countries.items():
        print(f"{code}- {country['name']}")

# توليد أرقام الهواتف
def generate_phone_numbers(count, country_code):
    country = countries.get(country_code)
    if not country:
        print(f"Sorry, the code {country_code} is not in the list.")
        return []
    
    country_dial_code = country['code']
    phone_length = country['length']
    prefixes = country['prefixes']
    phone_numbers = []
    
    for _ in range(count):
        prefix = random.choice(prefixes)
        number_length = phone_length - len(prefix)
        number = ''.join([str(random.randint(0, 9)) for _ in range(number_length)])
        full_number = f"+{country_dial_code}{prefix}{number}"
        phone_numbers.append(full_number)
    
    return phone_numbers

# تصفية الأرقام التي تحتوي على حساب Telegram
def filter_telegram_numbers(phone_numbers):
    valid_numbers = []
    invalid_numbers = []

    with app:
        for phone in phone_numbers:
            try:
                user = app.get_users(phone)
                print(f"Valid Telegram account found: {phone}")
                valid_numbers.append(phone)
            except Exception:
                print(f"Not a Telegram account: {phone}")
                invalid_numbers.append(phone)
    
    # حفظ النتائج في ملفات
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"valid_telegram_numbers_{current_time}.txt", 'w') as valid_file:
        valid_file.write("\n".join(valid_numbers))
    with open(f"invalid_numbers_{current_time}.txt", 'w') as invalid_file:
        invalid_file.write("\n".join(invalid_numbers))
    
    print(f"\nResults saved:")
    print(f"- Valid Telegram accounts: valid_telegram_numbers_{current_time}.txt")
    print(f"- Invalid numbers: invalid_numbers_{current_time}.txt")

# تشغيل البرنامج
print_touati_logo()
show_country_options()

selected_country_code = int(input("Enter the country number for which you want to generate numbers: "))
number_count = int(input("Enter the number of phone numbers you want to generate: "))

phone_numbers = generate_phone_numbers(number_count, selected_country_code)
print(f"\nGenerated {len(phone_numbers)} phone numbers. Checking for Telegram accounts...\n")

filter_telegram_numbers(phone_numbers)
