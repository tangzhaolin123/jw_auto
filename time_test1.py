from datetime import datetime
from datetime import timedelta
from time import sleep
# d_time = datetime.now() + timedelta(seconds=3600)
d_time1 = datetime.now()
sleep(10)
d_time2 = datetime.now()
a = d_time2 - d_time1
print (a<timedelta(seconds=5))
# a = 31
# total = 50
# rate = float(a/total)*100
# print (rate)