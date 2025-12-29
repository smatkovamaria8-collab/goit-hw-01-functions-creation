from datetime import datetime, timedelta

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    difference = date - today
    return difference.days

print(get_days_from_today('2025-12-20'))
