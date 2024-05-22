

# import datetime

# x = datetime.datetime.now()
# y = datetime.datetime(2023, 6, 15)
# print(x)
# print(x.day)
# print(y)
# print(y.strftime("%B"))


# from datetime import datetime
# import pytz

# tz = pytz.timezone("America/Los_Angeles")

# x = datetime.now(tz)

# print(x)


from datetime import datetime, timedelta

start = datetime.now()
end = start + timedelta(days=30)

# print(start)
# print(end)
# print(end - start)

x = end - start
print(x.days)
print(x.total_seconds())
print(x.total_seconds() / 60)
print(x.total_seconds() / 86400)
print(int(x.total_seconds() / 86400))