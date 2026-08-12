# ============================================================
# Q20. EXCEPTION AS e
# Catch an exception and display its message.
# ============================================================

try:
    number = int("Python")

except ValueError as e:
    print("Exception Message:", e)