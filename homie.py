# #Exercise 1
# from datetime import datetime, timedelta

# def get_days_from_today(date):
#     try:
#         date = datetime.strptime(date, "%Y-%m-%d").date()
#         today = datetime.today().date()
#         difference = date - today
#         return difference.days
#     except ValueError:
#         print("Please provide your date in this format: 'YYYY-MM-DD'")

# print(get_days_from_today("2025-12-20"))

# Exericise 2

#Я вирішила залишити цей варіант, бо перший не виходив

import random
    
def get_numbers_ticket(min, max, quantity):
    lottery_list = []
    if max > min:
        if min >1 and max <1000 and quantity <= ((max - min) +1):
            while len(lottery_list) < quantity:
                number = random.randint(min,max)
                lottery_list.append(number)
                new_list = set(lottery_list)
                lottery_list = list(new_list)
            return sorted(lottery_list)
        else:
            return lottery_list
    else:
        return []


print(get_numbers_ticket(10,14,5))

##Exercise 3

# import re

# def normalize_phone(phone_number):
#     pattern = r"\D+"
#     replac = r""
#     new_number= re.sub(pattern, replac, phone_number)
#     if new_number.startswith("38"):
#         new_number = f'+{new_number}'
#     elif new_number.startswith("0"):
#         new_number = f'+38{new_number}'
#     else:
#         pass
#     return new_number


# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
