import sys
import datetime
date1 = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')
date2 = datetime.datetime.today()
date = date1 - date2
print(date)

