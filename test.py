import requests
from pyfiglet import figlet_format
import random
from datetime import datetime

# توليد الشعار باستخدام pyfiglet
def print_touati_logo():
    logo = figlet_format('TOUATI', font='slant')  # يمكنك تغيير 'slant' إلى أي خط آخر
    print(logo)
    print("Auth:")
    print("Fb: https://web.facebook.com/touati.ayoub02/")

# عرض الشعار
print_touati_logo()

# قائمة الدول
countries = {
    1: {'name': 'Morocco', 'code': '212', 'prefixes': ['6', '7'], 'length': 9},
    2: {'name': 'Algeria', 'code': '213', 'prefixes': ['5', '6', '7'], 'length': 9},
    # يمكنك إضافة باقي الدول هنا
}

# التحقق من صحة الرقم باستخدام API
def validate_phone_number(number, access_key):
    url = "http://apilayer.net/api/validate"
    params = {
        "access_key": access_key,
        "number": number,
        "country_code": "",
        "format": 1
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("valid", False)
        else:
            print(f"⚠️ API Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")
        return False

# توليد أرقام الهواتف والتحقق من صحتها
def generate_and_validate_numbers(count, country_code, access_key):
    country = countries.get(country_code)
    if not country:
        print("Sorry, the code {} is not in the list.".format(country_code))
        return
    
    country_dial_code = country['code']
    phone_length = country['length']
    prefixes = country['prefixes']
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "valid_numbers_{}.txt".format(current_time)
    
    with open(file_name, 'w') as f:
        for i in range(count):
            prefix = random.choice(prefixes)
            number_length = phone_length - len(prefix)
            number = ''.join([str(random.randint(0, 9)) for _ in range(number_length)])
            full_number = "+{}{}{}".format(country_dial_code, prefix, number)
            
            # التحقق من صحة الرقم
            if validate_phone_number(full_number, access_key):
                f.write("{}\n".format(full_number))
                print(f"✅ {full_number} (Valid)")
            else:
                print(f"❌ {full_number} (Invalid)")
    
    print("Valid numbers saved in file {}".format(file_name))

# عرض قائمة الدول
def show_country_options():
    print("Choose a country to generate phone numbers:")
    for code, country in countries.items():
        print("{}- {}".format(code, country['name']))

# تشغيل البرنامج
show_country_options()
selected_country_code = int(input("Enter the country number for which you want to generate numbers: "))
number_count = int(input("Enter the number of phone numbers you want to generate: "))

# أدخل مفتاح الوصول الخاص بـ NumVerify
access_key = "dbc1bacbc62876fdca7a4f8ed2dc19d5"

# استدعاء الدالة
generate_and_validate_numbers(number_count, selected_country_code, access_key)
