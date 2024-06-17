#s24013 time_cal.py
#現在時刻と2024/6のカレンダーを表示する
#

import datetime
import calendar as cal
now = datetime.datetime.now()
print(now.strftime("%Y年%m月%d日 %H:%M:%S"))
print(cal.month(2024,6))
