# #Exercise 1
# from datetime import datetime, timedelta

# def get_days_from_today(date):
#     try:
#         date = datetime.strptime(date, "%Y-%m-%d").date()
#         today = datetime.today().date()
#         difference = date - today
#         return difference.days
#     except TypeError:
#         print("Please provide your date in this format: 'YYYY-MM-DD'")

# print(get_days_from_today("2025-12-20"))

#Exericise 2
#Спочатку я зробила ось так:

# import random

# def get_numbers_ticket(min, max, quantity):
#     lottery_list = []
#     if min >1 and max <1000:
#         for number in range(quantity):
#             number = random.randint(min,max)
#             while number not in lottery_list:
#                 lottery_list.append(number)
#                 break
#             else:
#                 number = random.randint(min,max)
#                 lottery_list.append(number)
#                 continue
#         return sorted(lottery_list)
#     else:
#         return lottery_list

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