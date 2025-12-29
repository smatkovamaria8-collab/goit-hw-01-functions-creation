from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = date - today
        return difference.days
    except TypeError:
        print("Please provide your date in this format: 'YYYY-MM-DD'")

print(get_days_from_today(2025-12-20))
