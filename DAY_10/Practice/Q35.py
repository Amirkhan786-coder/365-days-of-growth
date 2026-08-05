# Question:
# Use the datetime module to display the current date and time
# in the format DD-MM-YYYY HH:MM:SS.

from datetime import datetime

current = datetime.now()

formatted = current.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date & Time:", formatted)