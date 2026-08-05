# Question:
# Import the calendar module and display the calendar of the current month.

import calendar
import datetime

today = datetime.date.today()

print(calendar.month(today.year, today.month))