from _datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = datetime.strftime(now, '%d')
day_string = datetime.strftime(now, '%A')

given_time = '11 August 2045 Hour 23:11:10'
# defining parameters to get data wanted form
result = datetime.strptime(given_time, '%d %B %Y hour %H:%M:%S')

print(hour)
print(minute)
print(now)
print(day)
print(day_string)
print(result)
print(result.hour)
print(result.year)
