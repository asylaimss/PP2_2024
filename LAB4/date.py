#1
from datetime import date, timedelta
print(date.today() - timedelta(5))

#2
from datetime import date, timedelta
print(date.today() - timedelta(1)," ", date.today()," ", date.today() + timedelta(1))

#3
import datetime
print(datetime.datetime.today().replace(microsecond = 0))

#4
import datetime
a = datetime.datetime.now()
b = datetime.datetime(2023,2,19,22,28,30)
c = a - b
seconds = c.total_seconds()
print(seconds)