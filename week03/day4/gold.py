import datetime
# If needed: pip install holidays
import holidays

us_holidays = holidays.UnitedStates()

def next_holiday_info():
    today = datetime.date.today()
    # iterate over next 365 days to find the next holiday
    for i in range(1, 366):
        day = today + datetime.timedelta(days=i)
        if day in us_holidays:
            print(f"Today is {today}, the next holiday is {us_holidays[day]} on {day}, which is {i} days away.")
            break

next_holiday_info()
