#Exercise 1
from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = date - today
        return difference.days
    except TypeError:
        print("Please provide your date in this format: 'YYYY-MM-DD'")

print(get_days_from_today("2025-12-20"))

#Exericise 2
#Спочатку я зробила ось так:

import random

def get_numbers_ticket(min, max, quantity):
    lottery_list = []
    if min >1 and max <1000:
        for number in range(quantity):
            number = random.randint(min,max)
            while number not in lottery_list:
                lottery_list.append(number)
                break
            else:
                number = random.randint(min,max)
                lottery_list.append(number)
                continue
        return sorted(lottery_list)
    else:
        return lottery_list

#А потім подумала і зробила ось так:

import random
    
def get_numbers_ticket(min, max, quantity):
    lottery_list = []
    if min >1 and max <1000:
        while len(lottery_list) < quantity:
            number = random.randint(min,max)
            lottery_list.append(number)
            set(lottery_list)
        return sorted(lottery_list)
    else:
        return lottery_list

print(get_numbers_ticket(2,100,8))

#Exercise 3

import re

def normalize_phone(phone_number):
    new_list = []
    pattern = r"\D+"
    replac = r""
    for item in phone_number:
        new_number = re.sub(pattern, replac, item)
        if new_number.startswith("38"):
            new_number = f'+{new_number}'
        elif new_number.startswith("0"):
            new_number = f'+38{new_number}'
        else:
            pass
        new_list.append(new_number)

    return new_list


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print(normalize_phone(raw_numbers))