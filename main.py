from datetime import datetime, timedelta

day_today = datetime.now()
estimate = day_today + timedelta(days = 90)

print(f'90 days from today {day_today} will be {estimate}')

#Version 2

date = datetime(2024,10,1)
reverse = date - timedelta(days = 90)
if reverse < day_today:
    print('Not within time frame')
else:
    print('Within time frame')
